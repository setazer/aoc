import re
import time

from aocframework import AoCFramework


def manhattan(pos1, pos2):
    return abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])


class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def pos(self):
        return self.x, self.y

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x=},{self.y=})"

class Beacon(Point):
    pass

class Sensor(Point):
    def __init__(self, x, y, nearest_beacon:Beacon):
        super().__init__(x, y)
        self.range = manhattan(self.pos, nearest_beacon.pos)

    def __repr__(self):
        return f'{super().__repr__()[:-1]},{self.range=})'

    def in_range(self, pos):
        return manhattan(pos, self.pos) <= self.range


re_parse = re.compile(r"Sensor at x=(?P<Sx>-?\d+), y=(?P<Sy>-?\d+): closest beacon is at x=(?P<Bx>-?\d+), y=(?P<By>-?\d+)")


class Range:
    def __init__(self, min, max):
        self.min, self.max = min, max

    def __repr__(self):
        return f"Range({self.min=}, {self.max=})"

    def __contains__(self, item):
        return self.min <= item <= self.max

    def __iter__(self):
        return iter(range(self.min, self.max+1))

    def __or__(self, other):
        if isinstance(other, Range):
            if (self.min <= other.min <= self.max
                    or other.min <= self.min <= other.max
                    or self.min-other.max == 1
                    or self.max-other.min == 1):
                return Range(min(self.min, other.min), max(self.max, other.max))
        return None

    def __len__(self):
        return self.max - self.min + 1


class RangeAcc:
    def __init__(self):
        self.ranges = set()

    def __repr__(self):
        return f"Ranges({self.ranges})"

    def __len__(self):
        return sum(len(r) for r in self.ranges)

    def add_range(self, new):
        added_range = new

        if not self.ranges:
            self.ranges.add(added_range)
            return

        for item in self.ranges.copy():
            expanded = added_range | item
            if expanded is not None:
                self.ranges.discard(item)
                added_range = expanded
            else:
                continue
        self.ranges.add(added_range)


class DayPart1(AoCFramework):
    test_cases = (
        ("""Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""", 26),
    )
    known_result = 5125700

    def go(self):
        field = self.init_field()
        scan_y = 10
        if not self.test:
            scan_y = 2000000
        racc = RangeAcc()
        for obj in field.values():
            if not isinstance(obj, Sensor):
                continue

            scan_y_distance = abs(obj.y - scan_y)
            if obj.range < scan_y_distance:  # not in scanner range
                continue
            x_delta = obj.range - scan_y_distance
            min_x = obj.x - x_delta
            max_x = obj.x + x_delta

            r = Range(min_x, max_x)
            racc.add_range(r)
        if len(racc.ranges) == 1:
            r = racc.ranges.pop()
            return len(r) - sum(1 for (x, y) in field if r.min <= x <= r.max and y == scan_y)


    def init_field(self):
        field = {}
        for line in self.raw_puzzle_input.strip().splitlines():
            line_data = re_parse.match(line)
            Sx, Sy, Bx, By = tuple(map(int, line_data.groups()))
            beacon = Beacon(Bx, By)
            field[(Bx, By)] = beacon
            field[(Sx, Sy)] = Sensor(Sx, Sy, beacon)
        return field


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ("""Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""", 56000011),
    )
    known_result = None


    def init_field(self):
        field = {}
        for line in self.raw_puzzle_input.strip().splitlines():
            line_data = re_parse.match(line)
            Sx, Sy, Bx, By = tuple(map(int, line_data.groups()))
            beacon = Beacon(Bx, By)
            field[(Bx, By)] = beacon
            field[(Sx, Sy)] = Sensor(Sx, Sy, beacon)
        return field

    def go(self):
        field = self.init_field()
        full_filled_x = Range(0, 20)
        START = time.perf_counter()
        scan_min_y = 0
        scan_max_y = 20
        if not self.test:
            full_filled_x = Range(0, 4000000)
            scan_max_y = 4000000
        for scan_y in range(scan_min_y, scan_max_y + 1):
            racc = RangeAcc()
            for obj in field.values():
                if not isinstance(obj, Sensor):
                    continue

                scan_y_distance = abs(obj.y - scan_y)
                if obj.range < scan_y_distance:  # not in scanner range
                    continue
                x_delta = obj.range - scan_y_distance
                min_x = obj.x - x_delta
                max_x = obj.x + x_delta

                r = Range(min_x, max_x)
                racc.add_range(r)

            if any(coord in full_filled_x for r in racc.ranges for coord in (r.min, r.max)):
                for x in full_filled_x:
                    if all(x not in r for r in racc.ranges):
                        print(time.perf_counter() - START)
                        return x*4000000+scan_y


DayPart2()
