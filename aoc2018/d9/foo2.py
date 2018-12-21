from aocframework import AoCFramework
import blist
from time import time

class Day(AoCFramework):
    test_cases = ()

    def go(self):
        start = time()
        raw = self.puzzle_input.rstrip()
        raw_split = self.linesplitted
        players_count, marbles_total = [int(item) for item in raw.split() if item.isdigit()]
        marbles_total*=100
        board = blist.blist([2,1,0])
        scores = {player:0 for player in range(players_count)}
        current = 0

        for step in range(3, marbles_total+1):
            current_player = step % players_count
            # if step<50:
            #     print(step, '|', *[f'({item})' if board.index(item)==current else item for item in  board])
            if step % 23 == 0:
                scores[current_player] += step + board[current - 7]
                current =  (current - 7) % len(board)
                board.pop(current)
                board = board[current:]+board[:current]
                current=0
                continue

            new_marble_position = current + 2
            board.insert(new_marble_position % len(board), step)
            current=board.index(step)
            board = board[current:] + board[:current]
            current = 0
        print(time()-start)
        return max(scores.values())

Day()
