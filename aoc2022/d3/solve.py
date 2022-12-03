from functools import reduce
from itertools import tee

from aocframework import AoCFramework
from string import ascii_letters


PRIORITIES = [None, *ascii_letters]

class DayPart1(AoCFramework):
    test_cases = (
        ('''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw''', 157),
    )
    known_result = 7727

    def go(self):
        raw_split = self.linesplitted
        sum = 0
        for rucksack in raw_split:
            half = len(rucksack)//2
            comp1, comp2 = set(rucksack[:half]), set(rucksack[half:])
            common_item = tuple(comp1.intersection(comp2))[0]
            sum += ascii_letters.index(common_item) + 1

        return sum

DayPart1()


def triplets(iterable):
    a, b, c = [iter(iterable)]*3
    return zip(a, b, c)


class DayPart2(AoCFramework):
    test_cases = (
        ('''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw''', 70),
    )
    known_result = 2609

    def go(self):
        raw_split = self.linesplitted
        sum = 0
        for lines3 in triplets(raw_split):
            common_item = tuple(reduce(lambda x,y: x & y, map(set, lines3)))[0]
            sum += ascii_letters.index(common_item) + 1
        return sum


DayPart2()
