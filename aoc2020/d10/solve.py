from itertools import tee

from aocframework import AoCFramework

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


class DayPart1(AoCFramework):
    test_cases = (
        ('''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3''', 220),
    )
    known_result = 2112

    def go(self):
        adapters = sorted(map(int,self.linesplitted))
        adapters.insert(0,0)
        adapters.append(adapters[-1]+3)
        print(adapters)
        sum1 = sum(1 for a1, a2 in pairwise(adapters) if a2-a1 == 1)
        sum3 = sum(1 for a1, a2 in pairwise(adapters) if a2 - a1 == 3)
        return sum1*sum3


DayPart1()



class DayPart2(AoCFramework):
    test_cases = (
        ('''16
10
15
5
1
11
7
19
6
12
4''', 8),
        ('''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3''',19208),
    )
    known_result = 3022415986688

    def is_valid_arrangement(self, arrangement):
        extended_arr = [0, self.max_ad]
        extended_arr[1:1]=arrangement
        return all(a2-a1<=3 for a1,a2 in pairwise(extended_arr))

    def check_tree(self, arrangement: list):
        self.valids += 1
        for i, item in enumerate(arrangement):
            pass


    def go(self):
        self.valids=0
        adapters = sorted(map(int, self.linesplitted))
        adapters.insert(0, 0)
        # adapters.append(adapters[-1] + 3)
        neighbours = {item: list(filter(lambda x: x < item and item - x <=3, adapters))
                      for item in adapters}
        sums = {}
        rolling_sum = 0
        for key, values in neighbours.items():
            if not values:
                sums[key] = 1
            if len(values)==1:
                sums[key] = sums[values[0]]
            elif len(values)>1:
                sums[key] = sum(sums[value] for value in values)
        return max(sums.values())


DayPart2()
