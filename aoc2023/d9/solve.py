from itertools import pairwise, chain

from aocframework import AoCFramework


class DayPart1(AoCFramework):
    test_cases = (
        ('''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45''', 114),
    )
    known_result = 1637452029

    def go(self):
        raw_split = self.linesplitted
        seqs = [list(map(int, line.split(' '))) for line in raw_split]
        result = 0
        for seq in seqs:
            interpolations = [[y - x for x, y in pairwise(seq)]]
            while any(item != 0 for item in interpolations[-1]):
                interpolations.append([y - x for x, y in pairwise(interpolations[-1])])

            seq_last = sum([seq[-1]] + [inter[-1] for inter in interpolations])
            result += seq_last
        return result


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45''', 2),
    )
    known_result = 908

    def go(self):
        raw_split = self.linesplitted
        seqs = [list(reversed(list(map(int, line.split(' '))))) for line in raw_split]
        result = 0
        for seq in seqs:
            interpolations = [[y - x for x, y in pairwise(seq)]]
            while any(item != 0 for item in interpolations[-1]):
                interpolations.append([y - x for x, y in pairwise(interpolations[-1])])

            seq_last = sum([seq[-1]] + [inter[-1] for inter in interpolations])
            result += seq_last
        return result


DayPart2()
