use std::collections::HashSet;

type SolutionType = i32;
const PRIORITY: &str = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

#[aoc(day3, part1)]
pub fn part1(input: &str) -> SolutionType {
    let mut data:Vec<_> = vec![];
    for line in input.lines() {
        let half:usize = line.len()/2;
        data.push(line.split_at(half))
    }
    let mut sum:_ = 0;
    for (half1, half2) in data {
        let hs1 = half1.chars().collect::<HashSet<_>>();
        let hs2 = half2.chars().collect::<HashSet<_>>();
        let inter = hs1.intersection(&hs2).into_iter().next().unwrap();
        let priority = PRIORITY.find(*inter).unwrap() as SolutionType;
        sum+=priority;
    }
    sum
}

#[aoc(day3, part2)]
pub fn part2(input: &str) -> SolutionType {
    let data:Vec<_> = input.lines().collect();
    let mut sum:SolutionType = 0;
    for chunk in data.chunks_exact(3) {
        let elem = chunk.iter()
            .map(|&x| x.chars().collect::<HashSet<_>>())
            .reduce(|set1, set2| set1.intersection( &set2).copied().collect()).unwrap();
        sum+=PRIORITY.find(*elem.iter().next().unwrap()).unwrap() as i32;
    }
    sum
}

#[cfg(test)]
mod tests {
    use super::{
         part1,
         part2,
    };
    const TEST_INPUT:&str = "vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw";

    #[test]
    fn sample1() {
        assert_eq!(part1(TEST_INPUT) , 157);
    }

    #[test]
    fn sample2() {
        assert_eq!(part2(TEST_INPUT), 70);
    }
}