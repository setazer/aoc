from itertools import accumulate

from aocframework import AoCFramework

def gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm


def calc_nearest(timestamp, buses):
    timings = {bus: (bus - (timestamp % bus)) for bus in buses}
    return min(timings.items(), key=lambda x:x[1])


class DayPart1(AoCFramework):
    test_cases = (
        ('''939
7,13,x,x,59,x,31,19''', 295),
    )
    known_result = 2095

    def go(self):
        raw_split = self.linesplitted
        timestamp = int(raw_split[0])
        buses = list(map(int, filter(lambda x: x != 'x', raw_split[1].split(','))))
        bus_id, time_left = calc_nearest(timestamp, buses)
        return bus_id*time_left


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''
7,13,x,x,59,x,31,19''', 1068781),
        ('''
17,x,13,19''', 3417),
        ('''
67,7,59,61''', 754018),
        ('''
67,x,7,59,61''', 779210),
        ('''
67,7,x,59,61''', 1261476),
        ('''
1789,37,47,1889''', 1202161486),
    )
    known_result = None

    def go(self):
        raw_split = self.linesplitted[1].split(',')
        buses = [(i, int(bus)) for i, bus in enumerate(raw_split) if bus != 'x']
        offsets = list(accumulate(map(lambda x: x[1], buses), lcm))
        found = 1
        result = 0

        return 'Not solved'


DayPart2()
