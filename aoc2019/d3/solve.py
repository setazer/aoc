from operator import itemgetter

from aocframework import AoCFramework


class Point:
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other[0], self.y + other[1])

    def to_tuple(self):
        return self.x, self.y

    def __repr__(self):
        return f"Point <{self.x}, {self.y}>"


directions = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
}


def manhattan(point1: tuple, point2: tuple):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


class DayPart1(AoCFramework):
    test_cases = (
        ('''R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83''', 159),
        ('''R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7''', 135),
    )
    known_result = 8015

    def go(self):
        raw = self.puzzle_input.rstrip()
        raw_split = self.linesplitted
        grid = {}

        def parse_path(path, owner):
            path_parts = path.split(',')
            cur_point = Point(0, 0)
            for path_part in path_parts:
                d, l = path_part[0], int(path_part[1:])
                for i in range(l):
                    cur_point += directions[d]
                    cur_cell = grid.setdefault(cur_point.to_tuple(), set())
                    cur_cell.add(owner)

        for n, line in enumerate(raw_split):
            parse_path(line, n)
        intersections = list(filter(lambda x: len(grid[x]) > 1, grid))
        return min(manhattan(Point(0, 0).to_tuple(), grid_point)
                   for grid_point in intersections)


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83''', 610),
        ('''R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7''', 410),
    )
    known_result = 163676

    def go(self):
        raw = self.puzzle_input.rstrip()
        raw_split = self.linesplitted
        grid = {}

        def parse_path(path, owner):
            path_parts = path.split(',')
            cur_point = Point(0, 0)
            cur_l = 0
            for path_part in path_parts:
                d, l = path_part[0], int(path_part[1:])
                for i in range(l):
                    cur_point += directions[d]
                    cur_l += 1
                    cur_cell = grid.setdefault(cur_point.to_tuple(), {})
                    cur_cell.setdefault(owner, cur_l)

        for n, line in enumerate(raw_split):
            parse_path(line, n)
        intersections = list(filter(lambda x: len(grid[x]) > 1, grid))
        return sum(grid[min(intersections, key=lambda x: sum(grid[x].values()))].values())


DayPart2()
