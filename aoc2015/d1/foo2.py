from aocframework import AoCFramework

class Day(AoCFramework):
    test_cases = ()
    def go(self):
        floor = 0
        for n, item in enumerate(self.puzzle_input, 1):
            if item == "(":
                floor += 1
            elif item == ")":
                floor -= 1
                if floor == -1:
                    break
        return n
Day()
