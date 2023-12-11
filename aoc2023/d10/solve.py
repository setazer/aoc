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
        ('''''', ),
    )
    known_result = None

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

        return NotImplemented


DayPart2()
