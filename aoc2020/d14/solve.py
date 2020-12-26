from pprint import pprint

from aocframework import AoCFramework
import re

mem_re = re.compile(r"mem\[(\d+)] = (\d+)")

def masked_value(value, mask):
    bit_value = str(bin(int(value))[2:]).zfill(36)
    result = []
    for char, mask_ch in zip(bit_value, mask):
        result.append(char if mask_ch == 'X' else mask_ch)
    return int(''.join(result), 2)

def masked_address(address, mask):
    bit_value = str(bin(int(address))[2:]).zfill(36)
    floating = []
    for char, mask_ch in zip(bit_value, mask):
        if mask_ch == '1':
            floating.append('1')
        elif mask_ch == '0':
            floating.append(char)
        else:
            floating.append(mask_ch)
    for repl_num in range(2**floating.count('X')):
        rep_idx = 0
        rep_bit = list(reversed(str(bin(int(repl_num))[2:]).zfill(36)))
        result = []
        for char in reversed(floating):
            if char == 'X':
                result.insert(0, rep_bit[rep_idx])
                rep_idx += 1
            else:
                result.insert(0, char)
        yield int(''.join(result), 2)

class DayPart1(AoCFramework):
    test_cases = (
        ('''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0''', 165),
    )
    known_result = 5902420735773

    def go(self):
        mem = {}
        mask = None
        raw_split = self.linesplitted
        for line in raw_split:
            if line.startswith('mask'):
                mask = line.partition(' = ')[-1]
            elif line.startswith('mem'):
                mem_line = mem_re.search(line)
                address, value = mem_line.groups()
                value = masked_value(value, mask)
                mem[address] = value
        return sum(mem.values())


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1''', 208),
    )
    known_result = 3801988250775

    def go(self):
        mem = {}
        mask = None
        raw_split = self.linesplitted
        for line in raw_split:
            if line.startswith('mask'):
                mask = line.partition(' = ')[-1]
            elif line.startswith('mem'):
                mem_line = mem_re.search(line)
                address, value = mem_line.groups()
                addresses = masked_address(address, mask)
                for address in addresses:
                    mem[address] = int(value)
        return sum(mem.values())


DayPart2()
