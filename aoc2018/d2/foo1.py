from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = ()

    def go(self):
        raw = self.raw_puzzle_input
        raw_split = self.linesplitted
        twices = thrices = 0
        for box in raw_split:
            twices += (1 if any(box.count(char)==2 for char in box) else 0)
            thrices += (1 if any(box.count(char)==3 for char in box) else 0)
        return twices * thrices

Day()