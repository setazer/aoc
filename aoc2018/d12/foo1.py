from collections import Counter

from aocframework import AoCFramework

class Day(AoCFramework):
    test_cases = ()

    def go(self):
        raw = self.raw_puzzle_input.rstrip()
        raw_split = self.linesplitted
        lowest_index=0
        rules = {}
        field = ""
        for line_n, line in enumerate(raw_split):
            if line_n==0:
                field = line.replace("initial state: " , "")
                continue
            if line_n == 1:
                continue
            conds,_,result = line.split()
            rules[conds]=result
        def recount_field():
            nonlocal lowest_index,field
            while not field.startswith('.....'):
                lowest_index-=1
                field='.'+field
            while field.startswith('......'):
                lowest_index += 1
                field=field[1:]
            field = field.ljust(len(field) + 5, '.')
        field=field.ljust(len(field)+5,'.')
        for gen in range(20):
            new_field='..'
            recount_field()
            for st in range(len(field)-4):
                slice = field[st:st+5]
                new_field+=rules[slice]
            new_field+=".."
            field=new_field
            print(field)
        else:
            total_pot_val=0
            for n,c in enumerate(field,lowest_index):
                total_pot_val+=n if c == '#' else 0

        return total_pot_val

Day()