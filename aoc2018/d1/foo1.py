from aocframework import AoCFramework

class Day(AoCFramework):
    test_cases = ()
    def go(self):
        raw = self.puzzle_input.rstrip()
        raw_split = self.linesplitted
        cur_val = 0
        for item in raw_split:
            cur_val += int(item)
        return cur_val

Day()
