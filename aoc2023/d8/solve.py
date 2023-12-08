import math
from functools import reduce
from itertools import cycle

from aocframework import AoCFramework

def lcm(x, y):
   lcm = (x*y)//math.gcd(x,y)
   return lcm

class DayPart1(AoCFramework):
    test_cases = (
        ('''RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)''', 2),
        ('''LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)''', 6),
    )
    known_result = None

    def go(self):
        instructions = self.linesplitted[0]
        idx = 'LR'
        nodes = {}
        for line in self.linesplitted[2:]:
            node, _, paths = line.partition(' = ')
            path_l, _, path_r = paths.strip('()').partition(', ')
            nodes[node] = (path_l, path_r)

        cur_pos = 'AAA'
        for i, step in enumerate(cycle(instructions), 1):
            cur_pos = nodes[cur_pos][idx.index(step)]
            if cur_pos == 'ZZZ':
                return i


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)''', 6),
    )
    known_result = None

    def go(self):
        instructions = self.linesplitted[0]
        idx = 'LR'
        nodes = {}
        for line in self.linesplitted[2:]:
            node, _, paths = line.partition(' = ')
            path_l, _, path_r = paths.strip('()').partition(', ')
            nodes[node] = (path_l, path_r)

        positions = [node for node in nodes if node.endswith('A')]
        total = len(positions)
        last_exit_spotted = [(None, None)] * total
        loops_found = [False] * total
        for i, step in enumerate(cycle(instructions), 1):
            for j in range(total):
                positions[j] = nodes[positions[j]][idx.index(step)]
                if positions[j].endswith('Z'):
                    prev_pos = last_exit_spotted[j]
                    if prev_pos[0]:
                        new_distance = i - prev_pos[0]
                        last_exit_spotted[j] = (i, new_distance)
                        if prev_pos[0] == new_distance:
                            loops_found[j] = True
                            print('walker', j, 'loop found')
                    else:
                        last_exit_spotted[j] = (i, 0)
            if all(loops_found):
                break

        loop_lens = [item[1] for item in last_exit_spotted]
        return reduce(lambda x, y: lcm(x, y), loop_lens)


DayPart2()
