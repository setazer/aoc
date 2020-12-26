from itertools import product

from aocframework import AoCFramework


class Cell3D:
    def __init__(self, x, y, z, state=False):
        self.x, self.y, self.z = x, y, z
        self.state = state
        self.next_state = None

    def __repr__(self):
        return f"({self.x},{self.y},{self.z}: {self.state})"

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def coords(self):
        return self.x, self.y, self.z

    def sim(self):
        if self.next_state is not None:
            self.state = self.next_state

class Cell4D:
    def __init__(self, x, y, z, w, state=False):
        self.x, self.y, self.z, self.w = x, y, z, w
        self.state = state
        self.next_state = None

    def __repr__(self):
        return f"({self.x},{self.y},{self.z},{self.w}: {self.state})"

    def __eq__(self, other):
        return (self.x, self.y, self.z, self.w) == (other.x, other.y, other.z, self.w)

    def coords(self):
        return self.x, self.y, self.z, self.w

    def sim(self):
        if self.next_state is not None:
            self.state = self.next_state


class Grid3D:
    def __init__(self):
        self.grid = {}

    def print_slice(self, z=0):
        self.calc_borders()
        for x in range(self.min_x, self.max_x+1):
            for y in range(self.min_y, self.max_y+1):
                cell = self.grid.get((x, y, z))
                if cell and cell.state:
                    print('#', end='')
                else:
                    print('.', end='')
            print()

    def calc_borders(self):
        self.min_x = min(cell.x for cell in self.grid.values())-1
        self.min_y = min(cell.y for cell in self.grid.values())-1
        self.min_z = min(cell.z for cell in self.grid.values())-1
        self.max_x = max(cell.x for cell in self.grid.values())+1
        self.max_y = max(cell.y for cell in self.grid.values())+1
        self.max_z = max(cell.z for cell in self.grid.values())+1

    def active(self):
        return sum(cell.state for cell in self.grid.values())

    def add_cell(self, cell):
        self.grid.setdefault(cell.coords(), cell)

    def plan_next(self, cell):
        active = 0
        for off_x, off_y, off_z in product((-1,0,1), repeat=3):
            if off_x == off_y == off_z == 0:
                continue
            grid_cell = Cell3D(cell.x+off_x,
                               cell.y+off_y,
                               cell.z+off_z)
            if grid_cell.coords() in self.grid:
                active += self.grid[(cell.x+off_x,
                                     cell.y+off_y,
                                     cell.z+off_z)].state
        if active not in (2, 3) and cell.state:
            cell.next_state = False
        if active == 3 and not cell.state:
            cell.next_state = True
            self.add_cell(cell)

    def sim(self):
        self.calc_borders()
        for x in range(self.min_x, self.max_x+1):
            for y in range(self.min_y, self.max_y+1):
                for z in range(self.min_z, self.max_z+1):
                    cell = self.grid.get((x, y, z), Cell3D(x, y, z))
                    self.plan_next(cell)
        for cell in self.grid.values():
            cell.sim()


class Grid4D:
    def __init__(self):
        self.grid = {}

    def print_slice(self, z=0, w=0):
        self.calc_borders()
        for x in range(self.min_x, self.max_x+1):
            for y in range(self.min_y, self.max_y+1):
                cell = self.grid.get((x, y, z, w))
                if cell and cell.state:
                    print('#', end='')
                else:
                    print('.', end='')
            print()

    def calc_borders(self):
        self.min_x = min(cell.x for cell in self.grid.values())-1
        self.min_y = min(cell.y for cell in self.grid.values())-1
        self.min_z = min(cell.z for cell in self.grid.values())-1
        self.min_w = min(cell.w for cell in self.grid.values())-1
        self.max_x = max(cell.x for cell in self.grid.values())+1
        self.max_y = max(cell.y for cell in self.grid.values())+1
        self.max_z = max(cell.z for cell in self.grid.values())+1
        self.max_w = max(cell.w for cell in self.grid.values())+1

    def active(self):
        return sum(cell.state for cell in self.grid.values())

    def add_cell(self, cell):
        self.grid.setdefault(cell.coords(), cell)

    def plan_next(self, cell):
        active = 0
        for off_x, off_y, off_z, off_w in product((-1,0,1), repeat=4):
            if off_x == off_y == off_z == off_w == 0:
                continue
            grid_cell = Cell4D(cell.x+off_x,
                               cell.y+off_y,
                               cell.z+off_z,
                               cell.w+off_w)
            if grid_cell.coords() in self.grid:
                active += self.grid[(cell.x+off_x,
                                     cell.y+off_y,
                                     cell.z+off_z,
                                     cell.w+off_w)].state
        if active not in (2, 3) and cell.state:
            cell.next_state = False
        if active == 3 and not cell.state:
            cell.next_state = True
            self.add_cell(cell)

    def sim(self):
        self.calc_borders()
        for x in range(self.min_x, self.max_x+1):
            for y in range(self.min_y, self.max_y+1):
                for z in range(self.min_z, self.max_z+1):
                    for w in range(self.min_w, self.max_w+1):
                        cell = self.grid.get((x, y, z, w), Cell4D(x, y, z, w))
                        self.plan_next(cell)
        for cell in self.grid.values():
            cell.sim()


class DayPart1(AoCFramework):
    test_cases = (
        ('''.#.
..#
###''', 112),
    )
    known_result = 338

    def go(self):
        grid = Grid3D()
        for x, row in enumerate(self.linesplitted):
            for y, value in enumerate(row):
                if value == '#':
                    grid.add_cell(Cell3D(x, y, 0, True))
        for i in range(6):
            grid.sim()
        return grid.active()


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''.#.
..#
###''', 848),
    )
    known_result = 2440

    def go(self):
        grid = Grid4D()
        for x, row in enumerate(self.linesplitted):
            for y, value in enumerate(row):
                if value == '#':
                    grid.add_cell(Cell4D(x, y, 0, 0, True))
        for i in range(6):
            print('Simulating step',i)
            grid.sim()
        return grid.active()


DayPart2()
