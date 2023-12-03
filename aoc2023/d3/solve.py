from itertools import product, groupby

from aocframework import AoCFramework

# x ->
# y
# |
# V
offsets = (
    list(product((-1, 0, 1), repeat=2))
)
offsets.remove((0,0))


def check_surround(field, pos):
    for offset in offsets:
        offset_pos = (pos[0] + offset[0], pos[1] + offset[1])
        char = field.get(offset_pos)
        if not char: continue
        if not char.isdigit() and char != '.':
            return char, offset_pos
    return None

class DayPart1(AoCFramework):
    test_cases = (
        ('''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..''', 4361),
    )
    known_result = 539590

    def __init__(self, puzzle_input=None):
        super().__init__(puzzle_input)
        self.field = None



    def go(self):
        raw_split: str = self.linesplitted
        self.field = {(i, j): char for i, row in enumerate(raw_split) for j, char in enumerate(row)}
        max_x = len(self.linesplitted)
        max_y = len(self.linesplitted[0])
        numbers = []
        for i in range(max_x):
            parsed_number = ''
            tag = None
            for j in range(max_y):
                char: str = self.field[(i, j)]
                if char.isdigit():
                    parsed_number += char
                    if not tag:
                        tag = check_surround(self.field, (i, j))
                else:
                    if parsed_number:
                        numbers.append((parsed_number, tag))
                        parsed_number = ''
                        tag = None
            if parsed_number:
                numbers.append((parsed_number, tag))

        return sum(int(number) for number, tag in numbers if tag is not None)


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..''', 467835),
    )
    known_result = 80703636

    def go(self):
        raw_split: str = self.linesplitted
        self.field = {(i, j): char for i, row in enumerate(raw_split) for j, char in enumerate(row)}
        max_x = len(self.linesplitted)
        max_y = len(self.linesplitted[0])
        numbers = []
        for i in range(max_x):
            parsed_number = ''
            tag = None
            for j in range(max_y):
                char: str = self.field[(i, j)]
                if char.isdigit():
                    parsed_number += char
                    if not tag:
                        tag = check_surround(self.field, (i, j))
                else:
                    if parsed_number:
                        if tag:
                            numbers.append((int(parsed_number), tag))
                        parsed_number = ''
                        tag = None

            if parsed_number and tag:
                numbers.append((int(parsed_number), tag))
        result = 0
        numbers = sorted(numbers, key=lambda x: x[1])
        for key, group_items in groupby(numbers, lambda x: x[1]):
            group = list(group_items)
            if key and key[0] == '*' and len(group)==2:
                prod = group[0][0] * group[1][0]
                result += prod
        return result


DayPart2()
