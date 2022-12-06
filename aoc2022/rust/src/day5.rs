use std::str::FromStr;
use regex::Regex;

type SolutionType = String;

#[derive(Clone)]
pub struct Ship {
    warehouse:[String; 20],
}
impl Ship {
    pub fn act(&mut self, action:&Action) {
        for _ in 0..action.amount {
            let c = self.warehouse[action.source-1].pop().unwrap();
            self.warehouse[action.target-1].push(c);
        }
    }

    pub fn act_chunks(&mut self, action:&Action) {
        let length = self.warehouse[action.source-1].len();
        let chunk:String = self.warehouse[action.source-1][length-action.amount..].to_string();
        self.warehouse[action.target-1].push_str(chunk.as_str());
        self.warehouse[action.source-1] = self.warehouse[action.source-1][0..length-action.amount].to_string();
    }

    pub fn get_tops(&self) -> String {
        self.warehouse.iter().filter(|&s| !s.is_empty()).map(|s| s.chars().last().unwrap()).collect::<String>()
    }
}

#[derive(Debug)]
pub struct Action {
    amount: usize,
    source: usize,
    target: usize,
}

#[derive(Debug)]
pub struct ShipError;

impl FromStr for Ship {
    type Err = ShipError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let mut warehouse:[String;20] = Default::default();
        for line in s.lines().rev() {
            if &line[..3] == " 1 " { continue };
            for (col, idx) in (0..line.len()).step_by(4).enumerate() {
                let ship_crate = &line[idx..idx+3];
                if ship_crate.trim().is_empty() { continue };
                warehouse[col].push(ship_crate.chars().nth(1).unwrap());
            }
        }
        Ok(Ship{ warehouse })
    }
}

impl FromStr for Action{
    type Err = ShipError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let re = Regex::new(r"move (?P<amount>\d+) from (?P<source>\d+) to (?P<target>\d+)").unwrap();
        let res = re.captures(s);
        if let Some(captures) = res {
            return Ok(Action {
                amount: captures["amount"].parse::<usize>().unwrap(),
                source: captures["source"].parse::<usize>().unwrap(),
                target: captures["target"].parse::<usize>().unwrap(),
            })
        };
        Err(ShipError)
    }
}

#[aoc_generator(day5)]
pub fn input_generator(input: &str) -> (Ship, Vec<Action>) {

    let (crates_data, actions_data) = input.split_once("\n\n").unwrap();
    let ship = crates_data.parse::<Ship>().unwrap();
    let actions:Vec<_> = actions_data.trim().lines().map(|line| line.parse::<Action>().unwrap()).collect();
    (ship, actions)
}

#[aoc(day5, part1)]
pub fn part1(data: &(Ship, Vec<Action>)) -> SolutionType {
    let (ship, actions) = data;
    let mut actual_ship = ship.clone();
    for action in actions {
        actual_ship.act(action);
    };
    actual_ship.get_tops()
}

#[aoc(day5, part2)]
pub fn part2(data: &(Ship, Vec<Action>)) -> SolutionType {
    let (ship, actions) = data;
    let mut actual_ship = ship.clone();
    for action in actions {
        actual_ship.act_chunks(action);
    };
    actual_ship.get_tops()
}

#[cfg(test)]
mod tests {
    use super::{
        input_generator,
        part1,
        part2,
    };
    const TEST_INPUT:&str = "    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2";

    #[test]
    fn sample1() {
        assert_eq!(part1(&input_generator(TEST_INPUT)) , "CMZ".to_string());
    }

    #[test]
    fn sample2() {
        assert_eq!(part2(&input_generator(TEST_INPUT)), "MCD".to_string());
    }
}