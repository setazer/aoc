import itertools

from aocframework import AoCFramework


class Coord:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other):
        if isinstance(other, tuple):
            return Coord(self.x + other[0], self.y + other[1])
        raise TypeError

    def __eq__(self, other):
        if isinstance(other, Coord):
            return (self.x, self.y) == (other.x, other.y)
        raise TypeError

    def __repr__(self):
        return f"({self.x}, {self.y})"


DIRECTIONS = {
    'N': (0, -1),
    'NW': (-1, -1),
    'W': (-1, 0),
    'SW': (-1, 1),
    'S': (0, 1),
    'SE': (1, 1),
    'E': (1, 0),
    'NE': (1, -1),
}
MOVE_DIRECTIONS = [DIRECTIONS['N'], DIRECTIONS['S'], DIRECTIONS['W'], DIRECTIONS['E']]
DRAW_DIRECTIONS = {DIRECTIONS['N']: '^', DIRECTIONS['S']:'v', DIRECTIONS['W']:'<', DIRECTIONS['E']:'>'}

MOVE_CHECKS = {
    DIRECTIONS['N']: (DIRECTIONS['NW'], DIRECTIONS['N'], DIRECTIONS['NE']),
    DIRECTIONS['W']: (DIRECTIONS['NW'], DIRECTIONS['W'], DIRECTIONS['SW']),
    DIRECTIONS['S']: (DIRECTIONS['SW'], DIRECTIONS['S'], DIRECTIONS['SE']),
    DIRECTIONS['E']: (DIRECTIONS['NE'], DIRECTIONS['E'], DIRECTIONS['SE']),
}


class ProposedMove:
    def __init__(self, elf, coord):
        self.elf = elf
        self.coord = coord


class Elf:
    def __init__(self, x, y):
        self.pos = Coord(x, y)

    def __repr__(self):
        return f"Elf{self.pos}"

    def decide_move(self, occupied_positions, directions):
        if all(self.pos + d not in occupied_positions for d in DIRECTIONS.values()):
            return None

        for move_d in directions.copy():
            if all(self.pos + mc not in occupied_positions for mc in MOVE_CHECKS[move_d]):
                return ProposedMove(self, self.pos+move_d)

        return None

    def move(self, coord: Coord):
        self.pos = coord

def parse_field(field_data:str):
    for y, row in enumerate(field_data.splitlines()):
        for x, char in enumerate(row):
            if char == '#':
                yield Elf(x, y)

def get_boundaries(elves):
    min_x = min(coord.x for coord in elves)
    max_x = max(coord.x for coord in elves)
    min_y = min(coord.y for coord in elves)
    max_y = max(coord.y for coord in elves)
    return min_x, max_x, min_y, max_y

def calc_free_space(elves):
    min_x, max_x, min_y, max_y = get_boundaries(elves)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    return (width * height) - len(elves)

def draw_field(elves):
    min_x, max_x, min_y, max_y = get_boundaries(elves)
    for y in range(min_y, max_y + 1):
        print('.', end='')
        for x in range(min_x, max_x + 1):
            elf = elves.get(Coord(x, y))
            if elf:
                out = '#'  # DRAW_DIRECTIONS[elf.move_directions[0]]
            else:
                out = '.'
            print(out, end='')
        print('.')

class DayPart1(AoCFramework):
    test_cases = (
        ("""....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..""", 110),
    )
    known_result = 4195

    def go(self):
        elves = {elf.pos: elf for elf in parse_field(self.raw_puzzle_input)}
        directions = MOVE_DIRECTIONS.copy()
        draw_field(elves)
        for sim_round in range(0, 10):
            desired_moves = {}
            for elf in elves.values():
                proposed_move = elf.decide_move(elves, directions)
                if proposed_move:
                    desired_moves.setdefault(proposed_move.coord, []).append(proposed_move.elf)
            for target_coord, moving_elves in desired_moves.items():
                if len(moving_elves) == 1:
                    elf = moving_elves[0]
                    elves.pop(elf.pos)
                    elf.move(target_coord)
                    elves[target_coord] = elf
            directions.append(directions.pop(0))

            print()
            draw_field(elves)

        return calc_free_space(elves)


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ("""....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..""", 20),
    )
    known_result = 1069

    def go(self):
        elves = {elf.pos: elf for elf in parse_field(self.raw_puzzle_input)}
        directions = MOVE_DIRECTIONS.copy()
        draw_field(elves)
        for sim_round in itertools.count(1):
            desired_moves = {}
            for elf in elves.values():
                proposed_move = elf.decide_move(elves, directions)
                if proposed_move:
                    desired_moves.setdefault(proposed_move.coord, []).append(proposed_move.elf)
            if not desired_moves or all(len(m_elves) > 1 for m_elves in desired_moves.values()):
                print()
                draw_field(elves)
                return sim_round
            for target_coord, moving_elves in desired_moves.items():
                if len(moving_elves) == 1:
                    elf = moving_elves[0]
                    elves.pop(elf.pos)
                    elf.move(target_coord)
                    elves[target_coord] = elf
            directions.append(directions.pop(0))

            # print()
            # draw_field(elves)

DayPart2()
