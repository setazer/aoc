from aocframework import AoCFramework
from time import time
from blist import blist
class Day(AoCFramework):
    test_cases = ()
    def go(self):
        raw = self.puzzle_input.rstrip()
        raw_split = self.linesplitted
        iterations = int(raw)
        puzzle_input=list(raw)
        recipie_list = blist('37')
        elves = [0,1]
        start = time()
        i=0
        while True:
            i+=1
            if len(recipie_list)<15:
                print(recipie_list)
            new_recipie = blist(str(int(recipie_list[elves[0]])+int(recipie_list[elves[1]])))
            recipie_list.extend(new_recipie)
            for n,elf in enumerate(elves):
                elves[n] = (elf+int(recipie_list[elf])+1)%len(recipie_list)
            if list(recipie_list[-6:])==list(raw):
                return len(recipie_list)-len(puzzle_input)
            if list(recipie_list[-7:-1])==list(raw):
                return len(recipie_list)-len(puzzle_input)-1, recipie_list[-20:]
            if time()-start>30:
                print(i,len(recipie_list))
                start=time()
Day()
