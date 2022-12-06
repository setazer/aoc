from aocframework import AoCFramework


def solve(raw, window_size):
    for i in range(len(raw) - window_size):
        window = raw[i:i + window_size]
        if len(set(window)) == window_size:
            return i + window_size


class DayPart1(AoCFramework):
    test_cases = (
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
        ('nppdvjthqldpwncqszvftbrmjlhg', 6),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11),
    )
    known_result = 1757

    def go(self):
        raw = self.raw_puzzle_input
        return solve(raw, 4)


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 19),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 23),
        ('nppdvjthqldpwncqszvftbrmjlhg', 23),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 29),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 26),
    )
    known_result = 2950

    def go(self):
        raw = self.raw_puzzle_input
        return solve(raw, 14)


DayPart2()
