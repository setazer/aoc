from aocframework import AoCFramework

class Day(AoCFramework):
    test_cases = ()
    def go(self):
        raw = self.puzzle_input.rstrip()
        raw_split = self.linesplitted
        total_wrap=0
        for present in raw_split:
            l,w,h = map(int,present.split('x'))
            floor_top = l*w
            side1 = l*h
            side2 = w*h
            present_wrap=(2*(floor_top+side1+side2)+min(floor_top,side1,side2))
            total_wrap+=present_wrap
            # print(present,present_wrap)
        return total_wrap


Day()
