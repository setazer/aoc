from enum import Enum

from aocframework import AoCFramework


class Directions(Enum):
    NORTH = (0, -1)
    SOUTH = (0, 1)
    WEST = (-1, 0)
    EAST = (1, 0)


PIPES = {
    '|': {Directions.NORTH, Directions.SOUTH},
    '-': {Directions.EAST, Directions.WEST},
    'L': {Directions.NORTH, Directions.EAST},
    'J': {Directions.NORTH, Directions.WEST},
    '7': {Directions.SOUTH, Directions.WEST},
    'F': {Directions.SOUTH, Directions.EAST},
    '.': {},
    'S': set(Directions),
}


def draw_pipe(field, path):
    for y, row in enumerate(field):
        for x, char in enumerate(row):
            if (x, y) in path:
                char = '*'
            elif char == '.':
                char = ' '
            print(char, end='')
        print()


class DayPart1(AoCFramework):
    test_cases = (
        ('''-L|F7
7S-7|
L|7||
-L-J|
L|-JF''', 4),
        ('''..F7.
.FJ|.
SJ.L7
|F--J
LJ...''', 8)
    )
    known_result = 7093

    def go(self):
        field = self.linesplitted
        for y, row in enumerate(field):
            try:
                x = row.index('S')
                break
            except ValueError:
                continue
        start_pos = cur_pos = (x, y)
        go_dir = Directions.SOUTH
        steps = 0
        while True:
            go_tuple = go_dir.value
            cur_pos = (cur_pos[0]+go_tuple[0], cur_pos[1]+go_tuple[1])
            pipe = field[cur_pos[1]][cur_pos[0]]
            pipe_dirs = PIPES[pipe]
            from_dir = Directions((go_tuple[0]*-1, go_tuple[1]*-1))
            go_dir = next(iter(pipe_dirs - {from_dir}))
            steps += 1
            if cur_pos == start_pos:
                break

        return steps // 2


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........''', 4),
        ('''.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...''', 8),
        ('''FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L''', 10),
    )
    known_result = 407

    def go(self):
        field = self.linesplitted
        for y, row in enumerate(field):
            try:
                x = row.index('S')
                break
            except ValueError:
                continue
        start_pos = cur_pos = (x, y)
        go_dir = Directions.SOUTH
        path = {start_pos}
        steps = 0
        while True:
            go_tuple = go_dir.value
            cur_pos = (cur_pos[0]+go_tuple[0], cur_pos[1]+go_tuple[1])
            pipe = field[cur_pos[1]][cur_pos[0]]
            pipe_dirs = PIPES[pipe]
            from_dir = Directions((go_tuple[0]*-1, go_tuple[1]*-1))
            go_dir = next(iter(pipe_dirs - {from_dir}))
            steps += 1
            if cur_pos == start_pos:
                break
            path.add(cur_pos)
        insides = set()
        for y, row in enumerate(field):
            for x, char in enumerate(row):
                if (x, y) in path:
                    continue
                cur_x, cur_y = x, y
                intersections = 0
                while cur_x > 0 and cur_y > 0:
                    cur_x -= 1
                    cur_y -= 1
                    if (cur_x, cur_y) in path:
                        if field[cur_y][cur_x] in 'L7':
                            intersections += 2
                        else:
                            intersections += 1
                if intersections % 2 == 1:
                    insides.add((x, y))
        return len(insides)


DayPart2()
