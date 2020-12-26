import math
from collections import namedtuple

from aocframework import AoCFramework

def manhattan(x1,y1,x2,y2):
    return abs(x2-x1)+abs(y2-y1)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotate(self, direction, angle):
        target = Vector(self.x, self.y)
        if direction == 'L':
            for _ in range(angle//90):
                target.x, target.y = target.y, -target.x
        elif direction == 'R':
            for _ in range(angle//90):
                target.x, target.y = -target.y, target.x
        return target

    def __add__(self, other):
        return Vector(self.x+other.x,self.y+other.y)

    def __mul__(self, other):
        return Vector(self.x*other, self.y*other)

    def __iter__(self):
        return iter((self.x, self.y))

    def __repr__(self):
        return f'[{self.x},{self.y}]'


class Directions:
    EAST = Vector(1, 0)
    NORTH = Vector(0, -1)
    WEST = Vector(-1, 0)
    SOUTH = Vector(0, 1)


class Plane:
    def __init__(self):
        self.dir = Directions.EAST
        self.coords = Vector(0, 0)

    def do_action(self, instruction):
        action, *amount = instruction
        amount = int(''.join(amount))
        if action in 'NEWSF':
            self.move(action, amount)
        else:
            self.turn(action, amount)

    def move(self, direction, distance):
        directions = {
            'N': Directions.NORTH,
            'E': Directions.EAST,
            'W': Directions.WEST,
            'S': Directions.SOUTH,
            'F': self.dir,
        }
        move_vect = directions[direction]
        self.coords += move_vect*distance

    def turn(self, direction, angle):
        self.dir = self.dir.rotate(direction, angle)

    def __repr__(self):
        return f'Plane at {self.coords}'



class DayPart1(AoCFramework):
    test_cases = (
        ('''F10
N3
F7
R90
F11''', 25),
    )
    known_result = 1601

    def go(self):
        instructions = self.linesplitted
        plane = Plane()
        for instruction in instructions:
            plane.do_action(instruction)
        return manhattan(*plane.coords, 0, 0)


DayPart1()

class Plane2:
    def __init__(self):
        self.dir = Directions.EAST
        self.coords = Vector(0, 0)
        self.wp = Vector(10, -1)

    def do_action(self, instruction):
        action, *amount = instruction
        amount = int(''.join(amount))
        if action in 'NEWS':
            self.move_wp(action, amount)
        elif action == 'F':
            self.move(amount)
        else:
            self.turn_wp(action, amount)

    def move_wp(self, direction, distance):
        directions = {
            'N': Directions.NORTH,
            'E': Directions.EAST,
            'W': Directions.WEST,
            'S': Directions.SOUTH,
        }
        self.wp += directions[direction]*distance

    def turn_wp(self, side, angle):
        self.wp = self.wp.rotate(side,angle)

    def move(self, amount):
        self.coords += self.wp*amount









class DayPart2(AoCFramework):
    test_cases = (
        ('''F10
N3
F7
R90
F11''', 286),
    )
    known_result = 13340

    def go(self):
        instructions = self.linesplitted
        plane = Plane2()
        for instruction in instructions:
            plane.do_action(instruction)
        return manhattan(*plane.coords, 0, 0)


DayPart2()
