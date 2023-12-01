import re
from aocframework import AoCFramework


class DayPart1(AoCFramework):
    test_cases = [
        ('''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet''', 142),
    ]
    known_result = 55971

    def go(self):
        raw_split = self.linesplitted

        return sum(map(lambda x: int(x[0]+x[-1]), [re.sub('\D+','',line) for line in raw_split]))

DayPart1()

reps = {
    'one': '1',
    'two': '2',
    'six': '6',
    'four': '4',
    'five': '5',
    'nine': '9',
    'three': '3',
    'seven': '7',
    'eight': '8',
}

class DayPart2(AoCFramework):
    test_cases = [
        ('''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen''', 281),
    ]
    known_result = 54719


    def go(self):
        raw_split = self.linesplitted
        result = 0
        cl = cr = ''
        for line in raw_split:
            print(line, end=' ')

            for i, char in enumerate(line):
                if char.isdigit():
                    cl = char
                    break
                else:
                    if (found:=line[i:i+3]) in reps or (found:=line[i:i+4]) in reps or (found:=line[i:i+5]) in reps:
                        cl = reps[found]
                        break

            for i, char in enumerate(reversed(line)):
                if char.isdigit():
                    cr = char
                    break
                else:
                    if (found:=line[-i-3:-i or None]) in reps or (found:=line[-i-4:-i or None]) in reps or (found:=line[-i-5:-i or None]) in reps:
                        cr = reps[found]
                        break
            number = int(cl+cr)
            result += number
            print(number)
        return result


DayPart2()
