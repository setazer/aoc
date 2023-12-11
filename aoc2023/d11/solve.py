from itertools import permutations, combinations

from aocframework import AoCFramework


def manhattan(pos1, pos2):
    return abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])


def expand_space(galaxies, veritcal, horizontal, expansion_amount=2):
    for i, galaxy in enumerate(galaxies):
        gal_x, gal_y = galaxy
        for exp_ver in sorted(veritcal, reverse=True):
            if gal_x > exp_ver:
                gal_x += (expansion_amount - 1)

        for exp_hor in sorted(horizontal, reverse=True):
            if gal_y > exp_hor:
                gal_y += (expansion_amount - 1)
        galaxies[i] = (gal_x, gal_y)


class DayPart1(AoCFramework):
    test_cases = (
        ('''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....''', 374),
    )
    known_result = 9627977

    def go(self):
        raw_split: list = self.linesplitted
        expansions_hor = {i for i, row in enumerate(raw_split) if not row.count('#')}
        expansion_ver = set(range(len(raw_split[0])))
        for i, row in enumerate(raw_split):
            if not row.count('#'):
                continue
            for j, char in enumerate(row):
                if char == '#':
                    expansion_ver = expansion_ver - {j}

        galaxies = [(x,y) for y, row in enumerate(raw_split) for x, char in enumerate(row) if char == '#']
        expand_space(galaxies, expansion_ver, expansions_hor)
        return sum(manhattan(*pair) for pair in combinations(galaxies, 2))


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
# ('''...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....''', 1030),
# ('''...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....''', 8410),
    )
    known_result = 644248339497

    def go(self):
        raw_split: list = self.linesplitted
        expansions_hor = {i for i, row in enumerate(raw_split) if not row.count('#')}
        expansion_ver = set(range(len(raw_split[0])))
        for i, row in enumerate(raw_split):
            if not row.count('#'):
                continue
            for j, char in enumerate(row):
                if char == '#':
                    expansion_ver = expansion_ver - {j}

        galaxies = [(x,y) for y, row in enumerate(raw_split) for x, char in enumerate(row) if char == '#']
        expand_space(galaxies, expansion_ver, expansions_hor, 1000000)
        return sum(manhattan(*pair) for pair in combinations(galaxies, 2))


DayPart2()
