import enum

from aocframework import AoCFramework

class RPS(enum.Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Outcome(enum.Enum):
    WIN = 6
    DRAW = 3
    LOSE = 0

letters_to_shapes = {
    'A': RPS.ROCK,
    'X': RPS.ROCK,
    'B': RPS.PAPER,
    'Y': RPS.PAPER,
    'C': RPS.SCISSORS,
    'Z': RPS.SCISSORS,
}

pairs_to_outcome = {
    (RPS.ROCK, RPS.SCISSORS): Outcome.WIN,
    (RPS.PAPER, RPS.ROCK): Outcome.WIN,
    (RPS.SCISSORS, RPS.PAPER): Outcome.WIN,
    (RPS.ROCK, RPS.ROCK): Outcome.DRAW,
    (RPS.PAPER, RPS.PAPER): Outcome.DRAW,
    (RPS.SCISSORS, RPS.SCISSORS): Outcome.DRAW,
    (RPS.SCISSORS, RPS.ROCK): Outcome.LOSE,
    (RPS.ROCK, RPS.PAPER): Outcome.LOSE,
    (RPS.PAPER, RPS.SCISSORS): Outcome.LOSE,
}

def calc_rps(first:RPS, second:RPS):
    outcome = pairs_to_outcome[(second, first)]
    return outcome.value + second.value


class DayPart1(AoCFramework):
    test_cases = (
        ('''A Y
B X
C Z''', 15),
    )
    known_result = 15632

    def go(self):
        raw_split = self.linesplitted

        return sum((calc_rps(*[letters_to_shapes[item] for item in line.split()])for line in raw_split ))


DayPart1()

letters_to_outcome = {
    'X': Outcome.LOSE,
    'Y': Outcome.DRAW,
    'Z': Outcome.WIN,
}

shape_and_outcome_to_shape = {
    (RPS.ROCK, Outcome.WIN): RPS.PAPER,
    (RPS.ROCK, Outcome.DRAW): RPS.ROCK,
    (RPS.ROCK, Outcome.LOSE): RPS.SCISSORS,
    (RPS.PAPER, Outcome.WIN): RPS.SCISSORS,
    (RPS.PAPER, Outcome.DRAW): RPS.PAPER,
    (RPS.PAPER, Outcome.LOSE): RPS.ROCK,
    (RPS.SCISSORS, Outcome.WIN): RPS.ROCK,
    (RPS.SCISSORS, Outcome.DRAW): RPS.SCISSORS,
    (RPS.SCISSORS, Outcome.LOSE): RPS.PAPER,
}

def calc_points(first, outcome):
    return outcome.value + shape_and_outcome_to_shape[(first, outcome)].value

class DayPart2(AoCFramework):
    test_cases = (
        ('''A Y
B X
C Z''', 12),
    )
    known_result = 14416

    def go(self):
        raw_split = self.linesplitted
        result = 0
        for line in raw_split:
            first, _, outcome = line.partition(' ')
            first, outcome = letters_to_shapes[first], letters_to_outcome[outcome]
            result += calc_points(first, outcome)
        return result


DayPart2()
