import re

from aocframework import AoCFramework

test_case = '''Time:      7  15   30
Distance:  9  40  200'''


class DayPart1(AoCFramework):
    test_cases = (
        (test_case, 288),
    )
    known_result = None

    def get_parsed_input(self):
        times, _, distances = self.raw_puzzle_input.partition('\n')
        times = [int(item) for item in re.split('\W+', times)[1:]]
        distances = [int(item) for item in re.split('\W+', distances.strip())[1:]]
        return list(zip(times, distances))


    def go(self):
        races = self.get_parsed_input()
        result = 1
        for race_time, race_dist in races:
            race_wins = 0
            for time_pressed in range(1, race_time):
                time_left = race_time - time_pressed
                dist = time_left * time_pressed
                if dist > race_dist:
                    race_wins += 1
            result *= race_wins
        return result


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        (test_case, 71503),
    )
    known_result = None

    def go(self):
        races = DayPart1.get_parsed_input(self)
        one_race = list(zip(*races))
        race_time = int(''.join([str(item) for item in one_race[0]]))
        race_dist = int(''.join([str(item) for item in one_race[1]]))
        race_wins = 0
        for time_pressed in range(1, race_time):
            time_left = race_time - time_pressed
            dist = time_left * time_pressed
            if dist > race_dist:
                race_wins += 1
        return race_wins


DayPart2()
