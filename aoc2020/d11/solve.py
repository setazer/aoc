from aocframework import AoCFramework
from copy import deepcopy

class States:
    OCCUPIED = True
    FREE = False

class Seat:
    SEAT_LIMIT = 4
    def __init__(self, x=None, y=None, state=States.FREE):
        self.x = x
        self.y = y
        self.state=state
        self.adj_seats = []

    def read_adjacent(self, grid):
        adj_dirs = [
            (-1, -1), (0, -1), (1, -1),
            (-1, 0),           (1, 0),
            (-1, 1),  (0, 1),  (1, 1),
        ]
        for seat in tuple((self.x+adj_dir[0], self.y+adj_dir[1]) for adj_dir in adj_dirs):
            if seat in grid:
                self.adj_seats.append(grid[seat])

    def prepare_states(self):
        self.next_state = self.render()

    def switch(self):
        self.switched = (self.state != self.next_state)
        self.state = self.next_state

    def render(self):
        occupied = sum(seat.state == States.OCCUPIED for seat in self.adj_seats)
        if self.state == States.FREE and occupied == 0:
            return States.OCCUPIED
        if self.state == States.OCCUPIED and occupied >=self.SEAT_LIMIT:
            return States.FREE
        return self.state




    def __repr__(self):
        return f'Seat({self.x},{self.y})'

    def __eq__(self, other):
        return (
            self.x == other.x
            and self.y == other.y
        )
    def __add__(self, other):
        return Seat(self.x+other[0], self.y+other[1])

class DayPart1(AoCFramework):
    test_cases = (
        ('''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL''', 37),
    )
    known_result = 2108

    def go(self):
        raw_split = self.linesplitted
        seats = {(x,y): Seat(x,y) for y, row in enumerate(raw_split) for x, seat in enumerate(row) if seat=='L'}
        for coords, seat in seats.items():
            seat.read_adjacent(seats)
        while True:
            for seat in seats.values():
                seat.prepare_states()
            for seat in seats.values():
                seat.switch()
            if not any(seat.switched for seat in seats.values()):
                break
        return sum(seat.state == States.OCCUPIED for seat in seats.values())


DayPart1()


class Day2Seat(Seat):
    SEAT_LIMIT = 5
    def read_adjacent(self, grid):
        adj_dirs = [(1, 0), (0, 1),  (1, 1), (-1,1)]
        self.adj_seats.extend(list(filter(None, (self.find_adjacent(grid, direction) for direction in adj_dirs))))

    def find_adjacent(self, grid, direction):
        mul = 0
        grid_max_x = max(cell[0] for cell in grid)
        grid_max_y = max(cell[1] for cell in grid)
        while True:
            mul += 1
            seat_coords = (self.x+direction[0]*mul, self.y+direction[1]*mul)
            if seat_coords in grid:
                target_seat = grid[seat_coords]
                target_seat.adj_seats.append(self)
                return target_seat
            if not (
                0 <= seat_coords[0] <= grid_max_x
                and 0 <= seat_coords[1] <= grid_max_y
            ):
                break


class DayPart2(AoCFramework):
    test_cases = (
        ('''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL''', 26),
    )
    known_result = 1897

    def print_grid(self, grid):
        grid_max_x = max(cell[0] for cell in grid)
        grid_max_y = max(cell[1] for cell in grid)
        for y in range(grid_max_y+1):
            for x in range(grid_max_x+1):
                state = {True: '#', False: 'L', None: '.'}
                print(state[getattr(grid.get((x, y)), 'state', None)], end='')
            print()


    def go(self):
        raw_split = self.linesplitted
        seats = {(x, y): Day2Seat(x, y) for y, row in enumerate(raw_split) for x, seat in enumerate(row) if seat == 'L'}
        for i, (coords, seat) in enumerate(seats.items()):
            if i % 10 == 0:
                print(f"{i}/{len(seats)}")
            seat.read_adjacent(seats)
        while True:
            for seat in seats.values():
                seat.prepare_states()
            for seat in seats.values():
                seat.switch()
            self.print_grid(seats)
            if not any(seat.switched for seat in seats.values()):
                break

        return sum(seat.state == States.OCCUPIED for seat in seats.values())


DayPart2()
