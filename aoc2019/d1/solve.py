from aocframework import AoCFramework


class DayPart1(AoCFramework):
    test_cases = (
        ('12', 2),
        ('14', 2),
        ('1969', 654),
        ('100756', 33583)
    )
    known_result = 3406432

    def go(self):
        raw_split = self.linesplitted
        return sum(int(int(line) / 3) - 2 for line in raw_split)


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('14', 2),
        ('1969', 966),
        ('100756', 50346)
    )
    known_result = 5106777

    def go(self):
        raw_split = self.linesplitted
        return sum(self.total_fuel(line) for line in raw_split)

    def total_fuel(self, part):
        total = 0
        part_sum = int(int(part) / 3) - 2
        if part_sum >= 0:
            return part_sum + self.total_fuel(part_sum)
        else:
            return total


DayPart2()
