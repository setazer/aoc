from aocframework import AoCFramework


def opcode1(lst, initial_index):
    first_pos = lst[initial_index + 1]
    second_pos = lst[initial_index + 2]
    target_pos = lst[initial_index + 3]
    lst[target_pos] = lst[first_pos] + lst[second_pos]


def opcode2(lst, initial_index):
    first_pos = lst[initial_index + 1]
    second_pos = lst[initial_index + 2]
    target_pos = lst[initial_index + 3]
    lst[target_pos] = lst[first_pos] * lst[second_pos]


class DayPart1(AoCFramework):
    test_cases = (
        ('1,0,0,0,99', '2,0,0,0,99'),
        ('2,3,0,3,99', '2,3,0,6,99'),
        ('2,4,4,5,99,0', '2,4,4,5,99,9801'),
        ('1,1,1,4,99,5,6,0,99', '30,1,1,4,2,5,6,0,99'),
    )
    known_result = 4090701

    def go(self):
        raw = self.puzzle_input.rstrip()
        raw_split = self.linesplitted
        program = list(map(int, raw.split(',')))
        if not self.test:
            program[1] = 12
            program[2] = 2
        cur_pos = 0
        while True:
            cur_op = program[cur_pos]
            if cur_op == 1:
                opcode1(program, cur_pos)
                cur_pos += 4
            elif cur_op == 2:
                opcode2(program, cur_pos)
                cur_pos += 4
            elif cur_op == 99:
                return ','.join(list(map(str, program)))
            else:
                return ','.join(["HALTED"] + list(map(str, program)))


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
    )
    known_result = 6421

    def go(self):
        raw = self.puzzle_input.rstrip()
        raw_split = self.linesplitted
        self.program = list(map(int, raw.split(',')))
        for i in range(100):
            for j in range(100):
                res, status = self.calculate(i, j)
                if res == 19690720:
                    return i * 100 + j

    def calculate(self, noun, verb):
        program = self.program[:]
        program[1] = noun
        program[2] = verb
        cur_pos = 0
        while True:
            cur_op = program[cur_pos]
            try:
                if cur_op == 1:
                    opcode1(program, cur_pos)
                    cur_pos += 4
                elif cur_op == 2:
                    opcode2(program, cur_pos)
                    cur_pos += 4
                elif cur_op == 99:
                    return program[0], 'OK'
                else:
                    return program[0], 'HALTED'
            except Exception:
                return program[0], 'FAILED'


DayPart2()
