type SolutionType = i32;

#[derive(Debug, Eq, PartialEq, Copy, Clone)]
pub enum Shape {
    Rock,
    Paper,
    Scissors,
}

pub enum Outcome {
    Win,
    Loss,
    Draw,
}

trait ShapeRelation {
    fn beats(&self) -> Self;
    fn beaten_by(&self) -> Self;
}
trait Points {
    fn points(&self) -> i32;
}
impl Points for Shape {
    fn points(&self) -> i32 {
        match *self {
            Shape::Rock=>1,
            Shape::Paper=>2,
            Shape::Scissors=>3,
        }
    }
}

impl Points for Outcome {
    fn points(&self) -> i32 {
        match *self {
            Outcome::Win=>6,
            Outcome::Draw=>3,
            Outcome::Loss=>0,
        }
    }
}

impl ShapeRelation for Shape {
    fn beats(&self) -> Self {
        match *self {
            Shape::Rock => Shape::Scissors,
            Shape::Scissors => Shape::Paper,
            Shape::Paper => Shape::Rock,
        }
    }
    fn beaten_by(&self) -> Self {
        match *self {
            Shape::Rock => Shape::Paper,
            Shape::Scissors => Shape::Rock,
            Shape::Paper => Shape::Scissors,
        }
    }
}

#[aoc_generator(day2, part1)]
pub fn input_generator_part1(input: &str) -> Vec<(Shape, Shape)> {
    let mut result:Vec<_> = vec![];
    for line in input.lines() {
        let (other_shape, self_shape) = line.split_once(' ').unwrap();
        let other_shape = match other_shape {
            "A" => Shape::Rock,
            "B" => Shape::Paper,
            "C" => Shape::Scissors,
            _ => unreachable!(),
        };
        let self_shape= match self_shape {
            "X" => Shape::Rock,
            "Y" => Shape::Paper,
            "Z" => Shape::Scissors,
            _ => unreachable!(),
        };
        result.push((self_shape, other_shape));
    }
    result
}

#[aoc_generator(day2, part2)]
pub fn input_generator_part2(input: &str) -> Vec<(Shape, Outcome)> {
        let mut result:Vec<_> = vec![];
    for line in input.lines() {
        let (other_shape, self_shape) = line.split_once(' ').unwrap();
        let other_shape = match other_shape {
            "A" => Shape::Rock,
            "B" => Shape::Paper,
            "C" => Shape::Scissors,
            _ => unreachable!(),
        };
        let desired_outcome= match self_shape {
            "X" => Outcome::Loss,
            "Y" => Outcome::Draw,
            "Z" => Outcome::Win,
            _ => unreachable!(),
        };
        result.push((other_shape, desired_outcome));
    }
    result
}

#[aoc(day2, part1)]
pub fn part1(data: &[(Shape, Shape)]) -> SolutionType {
    let mut result = 0;
    for (self_shape, other_shape) in data {
        let outcome = if *other_shape == self_shape.beats() {
                Outcome::Win
            } else if *other_shape == self_shape.beaten_by() {
                Outcome::Loss
            } else {Outcome::Draw};

        result += self_shape.points() + outcome.points()
    }
    result
}

#[aoc(day2, part2)]
pub fn part2(data: &[(Shape, Outcome)]) -> SolutionType {
    data
    .iter()
    .map(|(other, outcome)|
        match outcome {
            Outcome::Win => other.beaten_by(),
            Outcome::Loss => other.beats(),
            Outcome::Draw => *other,
        }.points() + outcome.points()
    ).sum()
}

#[cfg(test)]
mod tests {
    use super::{input_generator_part1, input_generator_part2, part1, part2};
    const TEST_INPUT:&str = "A Y
B X
C Z";

    #[test]
    fn sample1() {
        assert_eq!(part1(&input_generator_part1(TEST_INPUT)) , 15);
    }

    #[test]
    fn sample2() {
        assert_eq!(part2(&input_generator_part2(TEST_INPUT)), 12);
    }
}