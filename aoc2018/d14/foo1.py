from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = ()
    def go(self):
        raw = self.puzzle_input.rstrip()
        raw_split = self.linesplitted
        iterations = int(raw)
        recipie_list = '37'
        elves = [0,1]
        while len(recipie_list) < iterations + 10:
            if len(recipie_list)<15:
                print(recipie_list)
            new_recipie = str(int(recipie_list[elves[0]])+int(recipie_list[elves[1]]))
            recipie_list+=new_recipie
            for n,elf in enumerate(elves):
                elves[n] = (elf+int(recipie_list[elf])+1)%len(recipie_list)
        else:
            return ''.join(recipie_list[iterations:iterations+10])
Day()
