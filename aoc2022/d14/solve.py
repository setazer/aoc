from itertools import pairwise

from aocframework import AoCFramework


class SpawnBlocked(Exception):
    pass


class Field:
    max_y = 0

    def __init__(self):
        self.data = {}

    def __contains__(self, item):
        if self.is_infinite_floor(item):
            return True
        return item in self.data

    def __getitem__(self, item):
        if self.is_infinite_floor(item):
            return Wall(*item)
        return self.data[item]

    def get(self, item):
        try:
            return self[item]
        except KeyError:
            return None

    def __iter__(self):
        return iter(self.data)

    def is_infinite_floor(self, item):
        return item[1] >= self.max_y + 2

    def draw(self):
        min_x, max_x = min(x for (x,_) in self), max(x for (x,_) in self)
        min_y, max_y = min(y for (_,y) in self), max(y for (_,y) in self)
        for y in range(min_y, max_y+2):
            for x in range(min_x, max_x+1):
                item = self.get((x,y))
                if not item:
                    out = '.'
                elif isinstance(item, Sand):
                    out = 'o'
                elif isinstance(item, Wall):
                    out='#'
                print(out, end='')
            print()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()

    def spawn_sand(self):
        spawn_pos = (500, 0)
        if spawn_pos in self.data:
            raise SpawnBlocked
        sand = Sand(*spawn_pos)
        self.data[sand.pos] = sand
        return sand

    def init_walls(self, walls_data):
        for wall_data in walls_data.split('\n'):
            coords = [tuple(map(int, item.split(',', maxsplit=1))) for item in wall_data.split(' -> ')]
            for coord1, coord2 in pairwise(coords):
                startx, starty, endx, endy = *coord1, *coord2
                if startx > endx:
                    startx, endx = endx, startx
                if starty > endy:
                    starty, endy = endy, starty
                for x in range(startx, endx+1):
                    for y in range(starty, endy+1):
                        self.data[(x, y)] = Wall(x, y)
        self.max_y = max(y for (_, y) in self.data)

    def move_obj(self, obj_pos, target_pos):
        item = self.data[obj_pos]
        self.data[target_pos] = item
        item.x, item.y = target_pos
        del self.data[obj_pos]


class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def pos(self):
        return self.x, self.y

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x=},{self.y=}"


class FallenOver(Exception):
    pass


class Sand(Point):
    def fall(self, field: Field):
        for offset in ((0, 1), (-1, 1), (1, 1)):
            if (self.x+offset[0], self.y+offset[1]) in field:
                continue
            else:
                target_pos = (self.x+offset[0], self.y+offset[1])
                field.move_obj(self.pos, target_pos)
                return True
        return False


class Wall(Point):
    pass


class DayPart1(AoCFramework):
    test_cases = (
        ("""498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""", 24),
    )
    known_result = None

    def go(self):
        field = Field()
        field.init_walls(self.raw_puzzle_input.strip())
        try:
            while True:
                sand = field.spawn_sand()
                while sand.fall(field):
                    if sand.y >= field.max_y:
                        del field.data[sand.pos]
                        raise FallenOver
        except FallenOver:
            pass
        total_sand = sum(1 for item in field.values() if isinstance(item, Sand))
        field.draw()
        return total_sand


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ("""498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""", 93),
    )
    known_result = None

    def go(self):
        field = Field()
        field.init_walls(self.raw_puzzle_input.strip())
        try:
            while True:
                sand = field.spawn_sand()
                while sand.fall(field):
                    pass
        except SpawnBlocked:
            pass

        total_sand = sum(1 for item in field.values() if isinstance(item, Sand))
        field.draw()
        return total_sand


DayPart2()
