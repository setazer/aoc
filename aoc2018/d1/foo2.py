from aocframework import AoCFramework

class Day(AoCFramework):
    test_cases = ()
    def go(self):
        raw = self.puzzle_input.rstrip()
        raw_split = self.linesplitted
        cur_val = 0
        partial_values = set()
        twice_found = False
        while not twice_found:
            for item in raw_split:
                partial_sum = cur_val + int(item)
                if partial_sum not in partial_values:
                    partial_values.add(partial_sum)
                else:
                    twice_found = True
                    break
                cur_val += int(item)
        return cur_val

Day()
