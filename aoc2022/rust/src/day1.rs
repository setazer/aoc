
type SolutionType = i32;

#[aoc_generator(day1)]
pub fn input_generator(input: &str) -> Vec<SolutionType> {
    let elves_data: Vec<&str> = input.split("\n\n").collect();
    let elves_data: Vec<SolutionType> = elves_data.iter()
        .map(|x| x
            .split('\n')
            .map(|x|x.parse::<SolutionType>().unwrap())
            .sum())
        .collect();
    elves_data
}

#[aoc(day1, part1)]
pub fn part1(data: &[SolutionType]) -> SolutionType {
    *data.iter().max().expect("Has max always")
}

#[aoc(day1, part2)]
pub fn part2(data: &[SolutionType]) -> SolutionType {
    let mut elves_data: Vec<_> = data.into();
    elves_data.sort();
    elves_data.iter().rev().take(3).sum()
}

#[cfg(test)]
mod tests {
    use super::{input_generator, part1, part2};
    const TEST_INPUT:&str = "1000
2000
3000

4000

5000
6000

7000
8000
9000

10000";

    #[test]
    fn sample1() {
        assert_eq!(part1(&input_generator(TEST_INPUT)) , 24000);
    }

    #[test]
    fn sample2() {
        assert_eq!(part2(&input_generator(TEST_INPUT)), 45000);
    }
}