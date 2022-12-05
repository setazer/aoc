import re
from collections import namedtuple
from typing import List, Tuple

from aocframework import AoCFramework


Action = namedtuple('Action', 'amount, source, target')


def act(ship: Tuple[List[str]], action: Action):
    for _ in range(action.amount):
        ship[action.target-1].append(ship[action.source-1].pop())


def act2(ship: Tuple[List[str]], action: Action):
    moved = ship[action.source-1][-action.amount:]
    ship[action.target-1].extend(moved)
    ship[action.source - 1][-action.amount:] = []


def parse_input(input_data):
    crates_data, _, actions_data = input_data.partition('\n\n')
    crate_rows = crates_data.split('\n')
    crate_towers = (len(crate_rows[0])-3)//4+1
    ship = tuple([] for _ in range(crate_towers))
    for row in crate_rows:
        row_crates = [row[idx:idx + 3] for idx in range(0, len(row), 4)]
        if row_crates[0] == ' 1 ':
            break
        for col, crate in enumerate(row_crates):
            if not crate.strip():
                continue
            ship[col].insert(0, crate[1:2])
    actions = []
    for action in actions_data.strip().split('\n'):
        parsed_action = re.match(r'move (?P<amount>\d+) from (?P<source>\d+) to (?P<target>\d+)', action)
        actions.append(
            Action(
                int(parsed_action.group('amount')),
                int(parsed_action.group('source')),
                int(parsed_action.group('target')),
            )
        )
    return ship, actions


class DayPart1(AoCFramework):
    test_cases = (
        ('''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2''', 'CMZ'),
    )
    known_result = 'ZWHVFWQWW'

    def go(self):
        raw = self.raw_puzzle_input
        ship, actions = parse_input(raw)
        for action in actions:
            act(ship, action)
        result = ''.join([stack.pop() for stack in ship])
        return result


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2''', 'MCD'),
    )
    known_result = 'HZFZCCWWV'

    def go(self):
        raw = self.raw_puzzle_input
        ship, actions = parse_input(raw)
        for action in actions:
            act2(ship, action)
        result = ''.join([stack.pop() for stack in ship])
        return result


DayPart2()
