from aocframework import AoCFramework
from time import time

class Day(AoCFramework):
    test_cases = ()

    def go(self):
        raw = self.raw_puzzle_input.rstrip()
        raw_split = self.linesplitted
        chars = set(raw.lower())
        def react(polymer):
            changed_string = polymer
            for char in chars:
                changed_string=changed_string.replace(char.lower(),"").replace(char.upper(),"")
            if changed_string == polymer:
                return changed_string
            react(changed_string)
            return polymer!=changed_string, changed_string

        char_lens = {}
        start = time()
        for char in chars:
            poly_w_o_char = raw.replace(char.lower(),"").replace(char.upper(),"")
            reaction_going = True
            react_start=time()
            while reaction_going:
                reaction_going, poly_w_o_char = react(poly_w_o_char)
            print(time()-react_start)
            char_lens[char]=len(poly_w_o_char)
            # print(char,char_lens[char])
        print(time()-start)
        return min(char_lens.values())

Day()