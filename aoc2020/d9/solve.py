import itertools

from aocframework import AoCFramework


def check_number(number, preamble_numbers):
    for comb in itertools.combinations(preamble_numbers,2):
        if sum(comb) == number:
            return True
    return False



class DayPart1(AoCFramework):
    test_cases = (
        # ('', ),
    )
    known_result = 32321523

    def go(self):
        preamble = 25
        raw_split = list(map(int, self.linesplitted))
        for i, line in enumerate(raw_split):
            if i < preamble:
                continue
            if not check_number(line, raw_split[i-preamble:i]):
                return line



DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        # ('', ),
    )
    known_result = 4794981

    def go(self):
        raw_split = list(map(int,self.linesplitted))
        target = DayPart1.known_result
        for i,_ in enumerate(raw_split):
            for j in range(i+1,raw_split.index(target)):
                if sum(raw_split[i:j+1]) == target:
                    print(raw_split[i:j+1])
                    return min(raw_split[i:j+1])+max(raw_split[i:j+1])
                if sum(raw_split[i:j+1])> target:
                    break


DayPart2()
