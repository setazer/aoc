from itertools import combinations

from aocframework import AoCFramework


class DayPart1(AoCFramework):
    test_cases = [
        ('''1721
            979
            366
            299
            675
            1456''', 514579),
    ]
    known_result = 970816

    def go(self):
        raw_split = self.linesplitted
        combs = list(map(int, raw_split))
        for one, two in combinations(combs,2):
            if one + two == 2020:
                return one * two


DayPart1()


class DayPart2(AoCFramework):
    test_cases = [
        # ("""""", ),
    ]
    known_result = 96047280

    def go(self):
        raw_split = self.linesplitted
        combs = list(map(int, raw_split))
        for one, two, three in combinations(combs, 3):
            if one + two + three == 2020:
                return one * two * three


DayPart2()
