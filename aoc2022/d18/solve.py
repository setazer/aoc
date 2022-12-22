from aocframework import AoCFramework


class Coord:
    __slots__ = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def pos(self):
        return self.x, self.y, self.z

    def __add__(self, other):
        if isinstance(other, tuple):
            x,y,z = other
            return self.x + x, self.y + y, self.z + z


neighbours = {
    (0,0,1),
    (0,0,-1),
    (0,1,0),
    (0,-1,0),
    (1,0,0),
    (-1,0,0),
}


class DayPart1(AoCFramework):
    test_cases = (
        ("""2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""", 64),
    )
    known_result = 3390

    def go(self):
        drops = {}
        for line in self.linesplitted:
            x,y,z = tuple(map(int,line.split(',')))
            drops[(x,y,z)]=Coord(x, y, z)

        surface_area = sum(6-sum(drop+nei in drops for nei in neighbours) for drop in drops.values())
        return surface_area


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ("""2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""", 58),
    )
    known_result = None

    def go(self):
        drops = {}
        for line in self.linesplitted:
            x,y,z = tuple(map(int,line.split(',')))
            drops[(x,y,z)]=Coord(x, y, z)

        min_x = min(x for (x, *_) in drops)
        max_x = max(x for (x, *_) in drops)
        min_y = min(y for (_, y, _) in drops)
        max_y = max(y for (_, y, _) in drops)
        min_z = min(z for (*_, z) in drops)
        max_z = max(z for (*_, z) in drops)
        inside_stuff = {}
        for x in range(min_x,max_x+1):
            for y in range(min_y,max_y+1):
                for z in range(min_z,max_z+1):
                    if (
                            next(((dx,dy,dz) for (dx,dy,dz) in drops if dx==x and dy==y and dz>z), None)
                            and next(((dx,dy,dz) for (dx,dy,dz) in drops if dx==x and dy==y and dz<z), None)
                            and next(((dx,dy,dz) for (dx,dy,dz) in drops if dx==x and dy>y and dz==z), None)
                            and next(((dx,dy,dz) for (dx,dy,dz) in drops if dx==x and dy<y and dz==z), None)
                            and next(((dx,dy,dz) for (dx,dy,dz) in drops if dx>x and dy==y and dz==z), None)
                            and next(((dx,dy,dz) for (dx,dy,dz) in drops if dx<x and dy==y and dz==z), None)
                    ):
                        inside_stuff[(x,y,z)] = Coord(x,y,z)
        drops.update(inside_stuff)
        surface_area = sum(6-sum(drop+nei in drops for nei in neighbours) for drop in drops.values())
        return surface_area


DayPart2()
