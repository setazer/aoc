type SolutionType = usize;
const START:u8 = b'a';

pub fn unique_window_position(s: &str, n:usize) -> SolutionType {
    for i in 0..s.len()-n {
        let mut chars = [0;26];
        let window = &s[i..i+n];
        window.chars().map(|c| {
            let idx = (c as u8 - START) as usize;
            chars[idx]^=1; c}).for_each(drop);
        if chars.iter().sum::<usize>() == n {
            return i+n;
        }
    }
    0
}

#[aoc(day6, part1)]
pub fn part1(input: &str) -> SolutionType {
    unique_window_position(input, 4)
}

#[aoc(day6, part2)]
pub fn part2(input: &str) -> SolutionType {
    unique_window_position(input, 14)
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    #[test]
    fn sample1() {
        let test_cases = [
            ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
            ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
            ("nppdvjthqldpwncqszvftbrmjlhg", 6),
            ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
            ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
        ];
        for (test_input, expected) in test_cases {
                    assert_eq!(part1(test_input) , expected);
        }
    }

    #[test]
    fn sample2() {
        let test_cases = [
            ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
            ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
            ("nppdvjthqldpwncqszvftbrmjlhg", 23),
            ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
            ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
        ];
        for (test_input, expected) in test_cases {
                    assert_eq!(part2(test_input) , expected);
        }
    }
}