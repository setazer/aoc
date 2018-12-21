from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = ()

    def go(self):
        raw = self.puzzle_input.rstrip()
        raw_split = self.linesplitted

        def addr(reg, A, B, C):
            registers=reg[:]
            registers[C] = registers[A] + registers[B]
            return registers

        def addi(reg, A, B, C):
            registers=reg[:]
            registers[C] = registers[A] + B
            return registers

        def mulr(reg, A, B, C):
            registers=reg[:]
            registers[C] = registers[A] * registers[B]
            return registers

        def muli(reg, A, B, C):
            registers=reg[:]
            registers[C] = registers[A] * B
            return registers

        def banr(reg, A, B, C):
            registers=reg[:]
            registers[C] = registers[A] & registers[B]
            return registers

        def bani(reg, A, B, C):
            registers=reg[:]
            registers[C] = registers[A] & B
            return registers

        def borr(reg, A, B, C):
            registers=reg[:]
            registers[C] = registers[A] | registers[B]
            return registers

        def bori(reg, A, B, C):
            registers=reg[:]
            registers[C] = registers[A] | B
            return registers

        def setr(reg, A, B, C):
            registers=reg[:]
            registers[C] = registers[A]
            return registers

        def seti(reg, A, B, C):
            registers=reg[:]
            registers[C] = A
            return registers

        def gtir(reg, A, B, C):
            registers=reg[:]
            registers[C] = 1 if A > registers[B] else 0
            return registers

        def gtri(reg, A, B, C):
            registers=reg[:]
            registers[C] = 1 if registers[A] > B else 0
            return registers

        def gtrr(reg, A, B, C):
            registers = reg[:]
            registers[C] = 1 if registers[A] > registers[B] else 0
            return registers

        def eqir(reg, A, B, C):
            registers=reg[:]
            registers[C] = 1 if A == registers[B] else 0
            return registers

        def eqri(reg, A, B, C):
            registers=reg[:]
            registers[C] = 1 if registers[A] == B else 0
            return registers

        def eqrr(reg, A, B, C):
            registers=reg[:]
            registers[C] = 1 if registers[A] == registers[B] else 0
            return registers

        funcs = [addi, addr, muli, mulr, bani, banr, bori, borr, seti, setr, gtir, gtri, gtrr, eqir, eqri, eqrr]
        opcodes = {i:[] for i in range(16)}
        samples = []
        code = []
        registers=[0]*4
        recieving_sample = False
        current_sample = {'before': [], 'command': '', 'after': []}
        total_same_registers=0
        for line in raw_split:

            if not recieving_sample and line.startswith("Before: "):
                _, before_reg = line.split(' ', maxsplit=1)
                before_reg = list(map(int, before_reg.strip('[]').split(', ')))
                current_sample = {'before': before_reg, 'command': '', 'after': []}
                recieving_sample = True
            elif recieving_sample and line.startswith('After: '):
                _, after_reg = line.split(' ', maxsplit=1)
                after_reg = list(map(int, after_reg.strip(' []').split(', ')))
                current_sample['after'] = after_reg
                samples.append(current_sample)
                if current_sample['before']==current_sample['after']:
                    total_same_registers+=1
                recieving_sample = False
            elif recieving_sample:
                current_sample['opcode'],*current_sample['command'] = list(map(int, line.split()))
            elif line.strip():
                opcode,*command = list(map(int,line.split()))
                code.append((opcode,command))

        print(total_same_registers)
        opcode_funcs = funcs[:]
        for opcode in opcodes:
            opcode_samples = [sample for sample in samples if sample['opcode']==opcode]
            for func in opcode_funcs:
                if all(sample['after']==func(sample['before'],*sample['command']) for sample in opcode_samples):
                    opcodes[opcode].append(func)

        while sum(len(item) for item in opcodes.values())>len(opcodes):
            for remopcode,remfuncs in opcodes.items():
                if len(remfuncs)==1:
                    rem_func=remfuncs[0]
                    for opcode,opfuncs in opcodes.items():
                        if rem_func in opfuncs and opcode!=remopcode:
                            opfuncs.remove(rem_func)

        for opcode,cmd in code:
            registers=opcodes[opcode][0](registers,*cmd)

        return registers[0]


Day()
