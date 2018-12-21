from aocframework import AoCFramework

class Day(AoCFramework):
    test_cases = ()
    def go(self):
        raw = self.puzzle_input.rstrip()
        raw_split = self.linesplitted
        toggler = 0
        class SantaClass:
            x=0
            y=0
        santas = [SantaClass(),SantaClass()]
        houses={}
        for direction in raw:
            toggler = 1 - toggler
            if direction == ">":
                santas[toggler].x+=1
            elif direction == "<":
                santas[toggler].x-=1
            elif direction == "^":
                santas[toggler].y+=1
            elif direction == "v":
                santas[toggler].y-=1
            for santa in santas:
                houses[(santa.x,santa.y)]=houses.get((santa.x,santa.y),0)+1
        return len(houses)

Day()
