from aocframework import AoCFramework

class Day(AoCFramework):
    test_cases = ()
    def go(self):
        raw = self.puzzle_input.rstrip()
        raw_split = self.linesplitted
        cur_x = 0
        cur_y = 0
        houses={}
        for direction in raw:
            if direction == ">":
                cur_x+=1
            elif direction == "<":
                cur_x-=1
            elif direction == "^":
                cur_y+=1
            elif direction == "v":
                cur_y-=1
            houses[(cur_x,cur_y)]=houses.get((cur_x,cur_y),0)+1
        return len(houses)


Day()
