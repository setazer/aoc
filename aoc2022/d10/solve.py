from functools import partial

from aocframework import AoCFramework


class CPU:
    __slots__ = ('cycle', 'X', 'actions', 'magic_cycles', 'sprite_pos', 'display')

    def __init__(self):
        self.cycle = 0
        self.X = 0
        self.actions = []
        self.magic_cycles = {i: None for i in range(20, 221, 40)}
        self.addx(1)
        self.display = ''

    def add_action(self, method, value):
        if method == 'noop':
            to_add = [self.noop]
        elif method == 'addx':
            to_add = [self.noop, partial(self.addx, value)]
        self.actions.extend(to_add)

    def draw_sprite(self, pixel):
        if pixel in self.sprite_pos:
            return '#'
        return '.'

    def simulate(self):
        for i, action in enumerate(self.actions, 0):
            if self.cycle in self.magic_cycles:
                self.magic_cycles[self.cycle] = self.cycle*self.X
            self.display += self.draw_sprite(i % 40)
            action()
            if ((i + 1) % 40) == 0:
                self.display += '\n'
        self.display = self.display.rstrip()

    def noop(self):
        self.cycle += 1

    def addx(self, val):
        self.cycle += 1
        self.X += val
        self.sprite_pos = tuple(self.X-1+i for i in range(3))

    def signal_strength(self):
        return self.X*self.cycle


class DayPart1(AoCFramework):
    test_cases = (
        ('''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop''', 13140),
    )
    known_result = 13680

    def go(self):
        raw_split = self.linesplitted

        cpu = CPU()
        for line in raw_split:
            action, _, value = line.partition(' ')
            value = int(value) if value else value
            cpu.add_action(action, value)

        cpu.simulate()

        return sum(cpu.magic_cycles.values())


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop''', "##..##..##..##..##..##..##..##..##..##..\n"
         "###...###...###...###...###...###...###.\n"
         "####....####....####....####....####....\n"
         "#####.....#####.....#####.....#####.....\n"
         "######......######......######......####\n"
         "#######.......#######.......#######....."),
    )
    known_result = ("###..####..##..###..#..#.###..####.###..\n"
                    "#..#....#.#..#.#..#.#.#..#..#.#....#..#.\n"
                    "#..#...#..#....#..#.##...#..#.###..###..\n"
                    "###...#...#.##.###..#.#..###..#....#..#.\n"
                    "#....#....#..#.#....#.#..#....#....#..#.\n"
                    "#....####..###.#....#..#.#....####.###..")

    def go(self):
        raw_split = self.linesplitted

        cpu = CPU()
        for line in raw_split:
            action, _, value = line.partition(' ')
            value = int(value) if value else value
            cpu.add_action(action, value)

        cpu.simulate()
        return cpu.display


DayPart2()
