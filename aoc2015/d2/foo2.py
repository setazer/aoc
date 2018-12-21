from aocframework import AoCFramework

class Day(AoCFramework):
    test_cases = ()
    def go(self):
        raw = self.puzzle_input.rstrip()
        raw_split = self.linesplitted
        total_wrap = 0
        for present in raw_split:
            l, w, h = map(int, present.split('x'))
            wrap_ribbon=min(2*l+2*w,2*l+2*h,2*w+2*h)
            wrap_bow=l*w*h
            total_wrap += (wrap_ribbon+wrap_bow)
            # print(present,present_wrap)
        return total_wrap

Day()
