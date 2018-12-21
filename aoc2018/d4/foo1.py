from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = ()

    def go(self):
        raw = self.raw_puzzle_input
        raw_split = self.linesplitted
        shifts = sorted(raw_split)
        for action in shifts:

            pass
Day()