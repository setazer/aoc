from functools import reduce
from itertools import product

from aocframework import AoCFramework


class DayPart1(AoCFramework):
    test_cases = (
        ('''abc

a
b
c

ab
ac

a
a
a
a

b''', 11),
    )
    known_result = 6587

    def go(self):
        groups = list(map(set,map(lambda x: x.replace('\n',''),self.puzzle_input.split('\n\n'))))

        return sum(map(len,groups))


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''abc

a
b
c

ab
ac

a
a
a
a

b''', 6),
    )
    known_result = 3235

    def go(self):
        groups = self.puzzle_input.strip().split('\n\n')
        groups_splitted = list(map(lambda x: x.split('\n'), groups))
        groups_splitted_sorted = [[''.join(sorted(elem)) for elem in g] for g in groups_splitted]
        groups_sets = [list(map(set, group)) for group in groups_splitted]
        groups_sets_intesections = [reduce(lambda x,y: x & y, g) for g in groups_sets]
        groups_lens = list(map(len, groups_sets_intesections))
        return sum(groups_lens)


DayPart2()
