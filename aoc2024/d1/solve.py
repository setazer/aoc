from aocframework import AoCFramework


class DayPart1(AoCFramework):
    test_cases = (
        ('''3   4
4   3
2   5
1   3
3   9
3   3''', 11),
    )
    known_result = 2113135

    def _parse_data(self):
        raw_split = self.linesplitted
        l1, l2 = [], []
        for line in raw_split:
            v1, _, v2 = line.partition('   ')
            l1.append(int(v1))
            l2.append(int(v2))
        l1 = sorted(l1)
        l2 = sorted(l2)
        return l1, l2

    def go(self):
        l1, l2 = self._parse_data()
        result = sum(abs(v1 - v2) for v1, v2 in zip(l1, l2))
        return result


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''3   4
4   3
2   5
1   3
3   9
3   3''', 31),
    )
    known_result = 19097157

    def go(self):
        l1, l2 = DayPart1._parse_data(self)
        result = sum(v1 * l2.count(v1) for v1 in l1)
        return result


DayPart2()
