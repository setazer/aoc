from functools import reduce

from aocframework import AoCFramework


class DayPart1(AoCFramework):
    test_cases = (
        ('''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#''', 7),
    )
    known_result = 189

    def go(self):
        raw_split = self.linesplitted[1:]
        x = 0
        cntr = 0
        for y, row in enumerate(raw_split):
            x = (x + 3) % len(row)
            if row[x] == '#':
                cntr+=1
        return cntr


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#''', 336),
    )
    known_result = 1718180100

    def go(self):
        raw_split = self.linesplitted[1:]
        xs = [0, 0, 0, 0]
        x2 = 0
        offsets = [1, 3, 5, 7]
        cntrs = [0, 0, 0, 0, 0]
        for y, row in enumerate(raw_split):
            for i, x in enumerate(xs):
                xs[i] = (x + offsets[i]) % len(row)
                if row[xs[i]] == '#':
                    cntrs[i] += 1
            if y % 2 == 1:
                x2 = (x2 + 1) % len(row)
                if row[x2] == '#':
                    cntrs[4] += 1
        print(cntrs)
        return reduce(lambda x, y: x*y, cntrs)


DayPart2()
