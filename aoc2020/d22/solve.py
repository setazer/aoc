from aocframework import AoCFramework
from collections import deque


class Player:
    def __init__(self, cards):
        self.cards = deque(cards)

    def empty(self):
        return len(self.cards) == 0

    def get_card(self):
        return self.cards.popleft()

    def won(self, cards):
        self.cards.extend(cards)


class DayPart1(AoCFramework):
    test_cases = (
        ('''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10''', 306),
    )
    known_result = 31629

    def go(self):
        pl1_cards, pl2_cards = self.puzzle_input.strip().split('\n\n')
        pl1 = Player(map(int, pl1_cards.split('\n')[1:]))
        pl2 = Player(map(int, pl2_cards.split('\n')[1:]))
        while not (pl1.empty() or pl2.empty()):
            card1, card2 = pl1.get_card(), pl2.get_card()
            if card1 > card2:
                pl1.won([card1, card2])
            elif card2 > card1:
                pl2.won([card2, card1])
            else:
                print('OH')
        for player in [pl1, pl2]:
            if player.empty():
                continue
            return sum((mul+1)*card for mul, card in enumerate(reversed(player.cards)))


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        # ('', ),
    )
    known_result = None

    def go(self):
        raw_split = self.linesplitted
        return


DayPart2()
