
type SolutionType = i32;

#[aoc_generator(day1, part1)]
pub fn input_generator_part1(input: &str) -> Vec<SolutionType> {
    input.lines()
}

#[aoc_generator(day1, part2)]
pub fn input_generator_part2(input: &str) -> Vec<SolutionType> {
    input.lines()
}

#[aoc(day1, part1)]
pub fn part1(data: &[SolutionType]) -> SolutionType {
    0
}

#[aoc(day1, part2)]
pub fn part2(data: &[SolutionType]) -> SolutionType {
    0
}

#[cfg(test)]
mod tests {
    use super::{input_generator_part1, input_generator_part2, part1, part2};
    const TEST_INPUT:&str = "";

    #[test]
    fn sample1() {
        assert_eq!(part1(&input_generator_part1(TEST_INPUT)) , 0);
    }

    #[test]
    fn sample2() {
        assert_eq!(part2(&input_generator_part2(TEST_INPUT)), 0);
    }
}