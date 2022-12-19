import itertools
from typing import Set

from aocframework import AoCFramework


class Coord:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x:int = x
        self.y:int = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

class Vector(Coord):

    def __neg__(self):
        return Vector(-self.x,-self.y)


class Point(Coord):
    __slots__ = ('x', 'y')
    
    @property
    def pos(self):
        return self.x, self.y
    
    def move(self, vec:Vector):
        self.x += vec.x
        self.y += vec.y

class ShapeType:
    def __init__(self, shape_data:set):
        self.shape_data:Set[Point] = shape_data

    @classmethod
    def from_data(cls, shape_data:str):
        result = set()
        for y, row in enumerate(shape_data.splitlines()):
            for x, col in enumerate(row):
                if col == '#':
                    result.add(Point(x, y))
        max_y = max(point.y for point in result)
        for point in result:
            point.y -= max_y  # offsetting stuff up for easier spawn rules
        return cls(result)


class FieldBounds:
    __slots__ = ('min_x', 'min_y', 'max_x', 'max_y')

    def __init__(self, top_left:Coord, bottom_right:Coord):
        self.min_x = top_left.x
        self.min_y = top_left.y
        self.max_x = bottom_right.x
        self.max_y = bottom_right.y


class Field:
    def __init__(self, bounds: FieldBounds):
        self.bounds = bounds
        self.solid_points = set()

    def draw(self):
        for y in range(self.bounds.min_y, self.bounds.max_y+1):
            print('|',end='')
            for x in range(self.bounds.min_x, self.bounds.max_x+1):
                if (x,y) in self.solid_points:
                    out = '#'
                else:
                    out = ' '
                print(out, end='')
            print('|')

    def trim(self, trim_y):
        self.solid_points = {(x,y) for (x,y) in self.solid_points if y>trim_y}

    def spawn_shape(self, shape_type:ShapeType):
        return Shape(self.bounds.min_x+2, self.bounds.min_y-4, shape_type)

    def check_bounds(self, shape):
        return any(x < self.bounds.min_x
                   or x > self.bounds.max_x
                   # or y < self.bounds.min_y
                   or y > self.bounds.max_y
                   for (x, y) in shape.coords)

    def move_shape(self, vec, shape):
        shape.move(vec)
        if self.check_bounds(shape) or self.check_solid(shape):
            shape.move(-vec)
            return False
        return True

    def drop_shape(self, shape):
        return self.move_shape(Vector(0, 1), shape)

    def check_solid(self, shape):
        return any(point in self.solid_points
                   for point in shape.coords)

    def solidize_shape(self, shape):
        self.solid_points |= shape.coords
        self.bounds.min_y = min(self.bounds.min_y, *(y for (_, y) in shape.coords))
        # not working
        if all(
                any((x,y+coord_y) in self.solid_points for y in (0,1))
                for _,coord_y in shape.coords
                for x in range(self.bounds.min_x, self.bounds.max_x+1)):
            self.trim(shape.origin.y+1)


class Shape:
    __slots__ = ('origin', 'shape_type')

    def __init__(self, x, y, shape_type:ShapeType):
        self.origin = Point(x, y)
        self.shape_type = shape_type

    def __repr__(self):
        return f'Shape @ {self.origin!r}'

    @property
    def coords(self):
        return {(self.origin.x + point.x, self.origin.y + point.y) for point in self.shape_type.shape_data}

    def move(self, vec):
        self.origin.move(vec)


SHAPE_TYPES = {
    'hor': ShapeType.from_data("####"),
    'plus': ShapeType.from_data(""".#.
###
.#."""),
    'L-shape': ShapeType.from_data("""..#
..#
###"""),
    'vert': ShapeType.from_data("""#
#
#
#"""),
    'square':ShapeType.from_data("""##
##"""),
}


def gen_movement(jet_data):
    jets = ""
    jet_vec = {'>': Vector(1, 0), '<': Vector(-1, 0)}
    for vec in itertools.cycle(jet_data):
        yield jet_vec[vec]

def gen_shape():
    for shape_type in itertools.cycle(['hor', 'plus', 'L-shape', 'vert', 'square']):
        yield SHAPE_TYPES[shape_type]


class DayPart1(AoCFramework):
    test_cases = (
        (""">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>""", 3068),
    )
    known_result = 3073

    def go(self):
        jet_data = self.raw_puzzle_input.strip()
        jet_gen = gen_movement(jet_data)
        shape_gen = gen_shape()
        field = Field(FieldBounds(Coord(0,0),Coord(6,-1)))
        for i, shape_type in zip(range(2022), shape_gen):
            new_shape = field.spawn_shape(shape_type)
            solid = False
            while not solid:
                field.move_shape(next(jet_gen), new_shape)
                if field.drop_shape(new_shape):
                    continue
                field.solidize_shape(new_shape)
                solid = True
        if not self.test:
            field.draw()
            print()

        return -field.bounds.min_y


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        (""">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>""", 1514285714288),
    )
    known_result = None

    def go(self):
        jet_data = self.raw_puzzle_input.strip()
        jet_gen = gen_movement(jet_data)
        shape_gen = gen_shape()
        field = Field(FieldBounds(Coord(0,0),Coord(6,-1)))
        for i, shape_type in zip(range(1_000_000_000_000), shape_gen):
            new_shape = field.spawn_shape(shape_type)
            solid = False
            while not solid:
                field.move_shape(next(jet_gen), new_shape)
                if field.drop_shape(new_shape):
                    continue
                field.solidize_shape(new_shape)
                solid = True
        if not self.test:
            field.draw()
            print()

        return -field.bounds.min_y


DayPart2()
