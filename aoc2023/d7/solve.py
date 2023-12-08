from collections import Counter
from enum import Enum
from itertools import product

from aocframework import AoCFramework


def get_combo(cards):
    counter = Counter(cards)
    if len(counter) == 1:
        return Combos.FIVE_OF_A_KIND
    if any(value == 4 for value in counter.values()):
        return Combos.FOUR_OF_A_KIND
    if len(counter) == 2 and all(value in (2, 3) for value in counter.values()):
        return Combos.FULL_HOUSE
    if any(value == 3 for value in counter.values()):
        return Combos.THREE_OF_A_KIND
    if len(counter) == 3 and set(counter.values()) == {2, 1}:
        return Combos.TWO_PAIR
    if any(value == 2 for value in counter.values()):
        return Combos.ONE_PAIR
    return Combos.HIGH_CARD


class Combos(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


class Hand:
    CARDS = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
    def __init__(self, cards: str):
        if len(cards) != 5:
            raise ValueError
        self.cards = cards
        self._combo: Combos = None

    def __repr__(self):
        return f"{self.cards}: {self.combo}"

    def __hash__(self):
        return hash(self.cards)

    @property
    def combo(self):
        if not self._combo:
            self._combo = get_combo(self.cards)
        return self._combo

    def __gt__(self, other):
        if not isinstance(other, Hand):
            raise TypeError
        if self.combo != other.combo:
            return self.combo.value > other.combo.value

        for self_card, other_card in zip(self.cards, other.cards):
            if self_card == other_card:
                continue
            return self.CARDS.index(self_card) > self.CARDS.index(other_card)


class DayPart1(AoCFramework):
    test_cases = (
        ('''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483''', 6440),
    )
    known_result = 250453939

    def go(self):
        raw_split = self.linesplitted

        bids = {Hand(line.partition(' ')[0]): int(line.partition(' ')[-1]) for line in raw_split}
        win_table = sorted(bids)
        result = 0
        for i, hand in enumerate(win_table, 1):
            result += i * bids[hand]
        return result


DayPart1()


class Hand2(Hand):
    CARDS = ('J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A')
    @property
    def combo(self):
        if not self._combo:
            if 'J' in self.cards and self.cards.count('J') != 5:
                other_cards = set(self.cards) - {'J'}
                j_indexes = [i for i, card in enumerate(self.cards) if card == 'J']
                replacements = product(other_cards, repeat=len(j_indexes))
                max_combo = Combos.HIGH_CARD
                for replacement in replacements:
                    new_cards = self.cards[:]
                    for idx, new_card in zip(j_indexes, replacement):
                        new_cards = new_cards[:idx] + new_card + new_cards[idx+1:]
                    max_combo = max(max_combo, get_combo(new_cards), key=lambda x: x.value)
                self._combo = max_combo
            else:
                self._combo = get_combo(self.cards)
        return self._combo


class DayPart2(AoCFramework):
    test_cases = (
        ('''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483''', 5905),
    )
    known_result = None

    def go(self):
        raw_split = self.linesplitted

        bids = {Hand2(line.partition(' ')[0]): int(line.partition(' ')[-1]) for line in raw_split}
        win_table = sorted(bids)
        result = 0
        for i, hand in enumerate(win_table, 1):
            result += i * bids[hand]
        return result


DayPart2()
