import re

from aocframework import AoCFramework


class DayPart1(AoCFramework):
    test_cases = (
        ('''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11''', 13),
    )
    known_result = 25004

    def go(self):
        raw_split = self.linesplitted
        cards = {}
        for line in raw_split:
            card_num, _, card_data = line.partition(': ')
            card_num = card_num.partition(' ')[-1]
            winning_nums, _, card_nums = card_data.partition(' | ')
            winning_nums = set(int(item) for item in re.split('\W+', winning_nums.strip()))
            card_nums = set(int(item) for item in re.split('\W+', card_nums.strip()))
            cards[int(card_num)] = (winning_nums, card_nums)
        result = 0
        for winning_nums, card_nums in cards.values():
            inter = winning_nums.intersection(card_nums)
            card_value = 2**(len(inter)-1) if inter else 0
            result += card_value
        return result


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11''', 30),
    )
    known_result = 14427616

    def go(self):
        raw_split = self.linesplitted
        cards = {}
        for line in raw_split:
            card_id, _, card_data = line.partition(': ')
            card_id = card_id.partition(' ')[-1]
            winning_nums, _, card_nums = card_data.partition(' | ')
            winning_nums = set(int(item) for item in re.split('\W+', winning_nums.strip()))
            card_nums = set(int(item) for item in re.split('\W+', card_nums.strip()))
            cards[int(card_id)] = (winning_nums, card_nums)

        wins = {card_id: 1 for card_id in cards}
        for card_id, (winning_nums, card_nums) in cards.items():
            inter = winning_nums.intersection(card_nums)
            card_value = len(inter)
            for i in range(card_id+1, card_id+card_value+1):
                if cards.get(i):
                    wins[i] += wins[card_id]
        return sum(wins.values())


DayPart2()
