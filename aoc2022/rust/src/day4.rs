
type SolutionType = usize;

pub struct Range{
    start: usize,
    end: usize,
}

impl Range {
    fn from_string(s:&str) -> Self {
        let (start, end) = s.split_once('-').unwrap();
        Range {
            start:start.parse().unwrap(),
            end:end.parse().unwrap(),
        }

    }
    fn contains(&self, other: &Range) -> bool {
        self.start <= other.start && self.end >= other.end
    }
    fn intersects(&self, other: &Range) -> bool {
        (self.start <= other.end && other.end <= self.end)
        || (other.start <= self.end && self.end <= other.end)
    }
}

#[aoc_generator(day4)]
pub fn input_generator(input: &str) -> Vec<(Range,Range)> {
    let mut res:Vec<_> = vec![];
    for line in input.lines() {
        let (r1, r2) = line.split_once(',').unwrap();
        res.push((Range::from_string(r1), Range::from_string(r2)))
    }
    res
}

#[aoc(day4, part1)]
pub fn part1(data: &[(Range, Range)]) -> SolutionType {
    data.iter().map(|(r1,r2)| (r1.contains(r2) || r2.contains(r1))).filter(|&x| x).count()
}

#[aoc(day4, part2)]
pub fn part2(data: &[(Range, Range)]) -> SolutionType {
    data.iter().map(|(r1,r2)| r1.intersects(r2)).filter(|&x| x).count()
}

#[cfg(test)]
mod tests {
    use super::*;
    const TEST_INPUT:&str = "2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8";

    #[test]
    fn sample1() {
        assert_eq!(part1(&input_generator(TEST_INPUT)) , 2);
    }

    #[test]
    fn sample2() {
        assert_eq!(part2(&input_generator(TEST_INPUT)), 4);
    }
}