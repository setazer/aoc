from aocframework import AoCFramework


class Range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    @classmethod
    def from_string(cls, range_string):
        start = int(range_string.partition('-')[0])
        end = int(range_string.partition('-')[-1])
        return cls(start, end)

    def __contains__(self, other):
        if isinstance(other, Range):
            return self.start <= other.start and self.end >= other.end
        raise TypeError()

    def __and__(self, other):
        if isinstance(other, Range):
            return (
                    other in self
                    or self in other
                    or self.start <= other.start <= self.end
                    or self.start <= other.end <= self.end
                    or other.start <= self.start <= other.end
                    or other.start <= self.end <= other.end
            )


class DayPart1(AoCFramework):
    test_cases = (
        ('''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8''', 2),
    )
    known_result = 496

    def go(self):
        raw_split = self.linesplitted
        sum = 0
        for line in raw_split:
            range1, _, range2 = line.partition(',')
            range1, range2 = Range.from_string(range1), Range.from_string(range2)
            sum += range1 in range2 or range2 in range1
        return sum


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8''', 4),
    )
    known_result = 847

    def go(self):
        raw_split = self.linesplitted
        sum = 0
        for line in raw_split:
            range1, _, range2 = line.partition(',')
            range1, range2 = Range.from_string(range1), Range.from_string(range2)
            sum += range1 & range2
        return sum


DayPart2()
