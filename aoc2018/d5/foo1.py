from aocframework import AoCFramework
from time import time

class Day(AoCFramework):
    test_cases = ()

    def go(self):
        raw = self.raw_puzzle_input.rstrip()
        raw_split = self.linesplitted
        chars = set(raw.lower())
        def react(polymer):
            initial_string = polymer
            changed_string = polymer
            for char in chars:
                changed_string=changed_string.replace(f"{char.upper()}{char.lower()}","").replace(f"{char.lower()}{char.upper()}","")
            return initial_string!=changed_string, changed_string
        reaction_going = True
        poly=raw
        start=time()
        while reaction_going:
            reaction_going, poly = react(poly)
        print(raw)
        print(poly)
        print(time()-start)
        return len(poly)

Day()