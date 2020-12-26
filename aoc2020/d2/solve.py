from aocframework import AoCFramework


class DayPart1(AoCFramework):
    test_cases = (
        ('''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc''', 2),
    )
    known_result = 474

    def go(self):
        raw_split = self.linesplitted
        valid = 0
        for line in raw_split:
            policy, _, password = line.partition(': ')
            limits, _, letter = policy.partition(' ')
            lower, _, upper = limits.partition('-')
            lower, upper = map(int, [lower, upper])
            if lower <= password.count(letter) <= upper:
                valid += 1
        return valid


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc''', 1),
    )
    known_result = 745

    def go(self):
        raw_split = self.linesplitted
        valid = 0
        for line in raw_split:
            policy, _, password = line.partition(': ')
            limits, _, letter = policy.partition(' ')
            first, _, second = limits.partition('-')
            first, second = map(int, [first, second])
            if ((password[first-1] == letter or password[second-1] == letter)
                and (not (password[first-1] == letter and password[second-1] == letter))):
                valid += 1
        return valid


DayPart2()
