
fn parse_elves_data(input: &str) -> Vec<i32> {
    let elves_data: Vec<&str> = input.split("\n\n").collect();
    let elves_data: Vec<i32> = elves_data.iter().map(|x| x.split("\n").map(|x|x.parse::<i32>().unwrap()).sum()).collect();
    elves_data
}

#[aoc(day1, part1, Chars)]
pub fn part1(input: &str) -> i32 {
    let elves_data = parse_elves_data(input);
    *elves_data.iter().max().expect("Has max always")
}

#[aoc(day1, part2, Chars)]
pub fn part2(input: &str) -> i32 {
    let mut elves_data = parse_elves_data(input);
    elves_data.sort();
    elves_data.reverse();
    elves_data[..3].iter().sum()
}

#[cfg(test)]
mod tests {
    use super::{part1, part2};

    #[test]
    fn sample1() {
        assert_eq!(part1("1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"), 24000);
    }

    #[test]
    fn sample2() {
        assert_eq!(part2("1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"), 45000);
    }

}