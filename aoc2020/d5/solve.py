from itertools import product

from aocframework import AoCFramework

def decipher(board_pass):
    row, seat = board_pass[:-3], board_pass[-3:]
    row = int(row.translate({ord('B'):'1',ord('F'):'0'}), 2)
    seat = int(seat.translate({ord('R'):'1',ord('L'):'0'}), 2)
    return row, seat

def next_and_prev(seat):
    next_seat = list(seat)
    next_seat[1]+=1
    if next_seat[1]>7:
        next_seat[0]+=1
        next_seat[1]=0
    prev_seat = list(seat)
    prev_seat[1]-=1
    if prev_seat[1]<0:
        prev_seat[0]-=1
        prev_seat[1]=7
    return tuple(next_seat), tuple(prev_seat)

class DayPart1(AoCFramework):
    test_cases = (
        # ('', ),
    )
    known_result = 901

    def go(self):
        raw_split = self.linesplitted
        return max(map(lambda x: x[0] * 8 + x[1],map(decipher, raw_split)))


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        # ('', ),
    )
    known_result = 661

    def go(self):
        raw_split = self.linesplitted
        seats = set(map(decipher,raw_split))
        all_seats = set(product(range(128), range(8)))
        difference = all_seats - seats
        for seat in difference:
            n, p = next_and_prev(seat)
            if n in seats and p in seats:
                return seat[0]*8+seat[1]


DayPart2()
