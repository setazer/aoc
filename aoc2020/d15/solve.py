from aocframework import AoCFramework

def get_next(spoken, numbers):
    last_number = spoken[-1]
    if last_number not in spoken[:-1]:
        return 0
    else:
        prev_occurence = len(spoken[:-1]) - 1 - spoken[-2::-1].index(last_number)
        return (len(spoken)-1)-prev_occurence

class DayPart1(AoCFramework):
    test_cases = (
        ('0,3,6', 436),
        ('1,3,2', 1),
        ('2,1,3', 10),
        ('1,2,3', 27),
        ('2,3,1', 78),
        ('3,2,1', 438),
        ('3,1,2', 1836),
    )
    known_result = 447

    def go(self):
        numbers = list(map(int,self.puzzle_input.split(',')))
        spoken = []
        spoken.extend(numbers)
        while len(spoken)<2020:
            spoken.append(get_next(spoken, numbers))
        return spoken[-1]


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('', ),
    )
    known_result = None

    def go(self):
        numbers = list(map(int,self.puzzle_input.split(',')))
        spoken = []
        spoken.extend(numbers)
        # while len(spoken)<3000000:
        #     spoken.append(get_next(spoken, numbers))
        return 'Not solved'


DayPart2()
