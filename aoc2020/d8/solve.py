from aocframework import AoCFramework

class Parser:
    def __init__(self, operations):
        self.operations = operations
        self._acc = 0
        self.cur_index = 0

    def cur_op(self):
        return self.operations[self.cur_index]

    def nop(self, value):
        self.cur_index+=1

    def jmp(self, value):
        self.cur_index+=int(value)

    def acc(self, value):
        self._acc+=int(value)
        self.cur_index +=1

    def cmd(self):
        operation, _, value = self.cur_op().partition(' ')
        getattr(self, operation)(value)

    def mod_cmd(self, index):
        mapping = {
            'nop': 'jmp',
            'jmp': 'nop',
        }
        cmd = self.operations[index]
        operation, _,  value = cmd.partition(' ')
        operation = mapping[operation]
        self.operations[index] = ' '.join([operation, value])

    def find_loop(self):
        last_ops = []
        while True:
            if self.cur_index in last_ops:
                return True
            last_ops.append(self.cur_index)
            self.cmd()
            if self.cur_index == len(self.operations):
                return False

    def find_executable(self):
        orig_ops = self.operations.copy()
        for i, cmd in enumerate(orig_ops):
            self.operations = orig_ops.copy()
            self._acc = 0
            self.cur_index=0
            if not cmd.startswith('acc'):
                self.mod_cmd(i)
                if not self.find_loop():
                    return

class DayPart1(AoCFramework):
    test_cases = (
        ('''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6''', 5),
    )
    known_result = 1600

    def go(self):
        p = Parser(self.linesplitted)
        p.find_loop()
        return p._acc


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6''', 8),
    )
    known_result = 1543

    def go(self):
        p = Parser(self.linesplitted)
        p.find_executable()
        return p._acc


DayPart2()
