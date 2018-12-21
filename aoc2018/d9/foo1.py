from aocframework import AoCFramework

class Day(AoCFramework):
    test_cases = ()
    def go(self):
        raw = self.puzzle_input.rstrip()
        raw_split = self.linesplitted
        players_count, marbles_total = [int(item) for item in raw.split() if item.isdigit()]
        board = [0,2,1]
        scores = {player:0 for player in range(players_count)}
        current = 1

        for step in range(3, marbles_total+1):
            current_player = step % players_count
            # if step<50:
            #     print(step, '|', *[f'({item})' if board.index(item)==current else item for item in  board])
            if step % 23 == 0:
                scores[current_player] += step + board[current - 7]
                current =  (current - 7) % len(board)
                board.pop(current)
                continue

            new_marble_position = current + 2
            if new_marble_position == len(board):
                board.append(step)
                current = len(board)-1
            else:

                board.insert(new_marble_position % len(board), step)
                current=board.index(step)

        return max(scores.values())




Day()
