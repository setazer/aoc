from aocframework import AoCFramework


class DayPart1(AoCFramework):
    test_cases = (
        ('''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000''', 24000),
    )
    known_result = 70116

    def go(self):
        elves_raw = self.puzzle_input.split('\n\n')
        elves_data = [sum([int(elve_item) for elve_item in elve_items.split()]) for elve_items in elves_raw]
        return max(elves_data)


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('', ),
    )
    known_result = 206582

    def go(self):
        elves_raw = self.puzzle_input.split('\n\n')
        elves_data = [sum([int(elve_item) for elve_item in elve_items.split()]) for elve_items in elves_raw]
        return sum(sorted(elves_data,reverse=True)[:3])


DayPart2()
