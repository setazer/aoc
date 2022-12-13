from functools import cmp_to_key
from itertools import zip_longest

from aocframework import AoCFramework


def is_valid(iter1, iter2):
    for item1, item2 in zip_longest(iter1, iter2):
        if item1 == item2:
            continue
        if item1 is None:
            return True
        if item2 is None:
            return False
        if isinstance(item1, int) and isinstance(item2, int):
            return item1 < item2
        if isinstance(item1, int) and isinstance(item2, list):
            result = is_valid([item1], item2)
        elif isinstance(item1, list) and isinstance(item2, int):
            result = is_valid(item1, [item2])
        else:
            result = is_valid(item1, item2)
        if result is not None:
            return result


class DayPart1(AoCFramework):
    test_cases = (
        ('''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]''', 13),
    )
    known_result = None

    def go(self):
        pairs = self.raw_puzzle_input.split('\n\n')
        sum = 0
        for i,pair in enumerate(pairs,1):
            iter1 = eval(pair.partition('\n')[0])
            iter2 = eval(pair.partition('\n')[-1])
            if is_valid(iter1, iter2):
                sum+=i
        return sum


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]''', 140),
    )
    known_result = None

    def go(self):
        data = [eval(item) for item in self.raw_puzzle_input.split('\n') if item.strip()]
        extra_packets = [[[2]],[[6]]]
        data.extend(extra_packets)
        prod = 1
        result = sorted(data, key=cmp_to_key(self.my_cmp))
        for i, item in enumerate(result):
            if item in extra_packets:
                prod *= i+1
        return prod

    def my_cmp(self, a, b):
        result = is_valid(a, b)
        if result is None:
            return 0
        return -1 if result else 1


DayPart2()
