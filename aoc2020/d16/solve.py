from collections import defaultdict
from copy import deepcopy
from functools import partial
from operator import itemgetter

from aocframework import AoCFramework


def invalid_numbers_sum(ticket, ranges):
    tsum = 0
    for value in ticket:
        if not any(
                (r_min <= value <= r_max) for section, value_range in ranges.items() for r_min, r_max in
                value_range):
            tsum += value
    return tsum

def invalid_numbers(ticket, ranges):
    for value in ticket:
        if not any(
                (r_min <= value <= r_max) for section, value_range in ranges.items() for r_min, r_max in
                value_range):
            return True
    return False

def get_range_include(value, ranges_dict):
    for field, ranges in ranges_dict.items():
        for r_min, r_max in ranges:
            if r_min <= value <= r_max:
                return field

class DayPart1(AoCFramework):
    test_cases = (
        ('''class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12''', 71),
    )
    known_result = 28873

    def go(self):
        raw = self.puzzle_input
        ranges, my_ticket, other_tickets = raw.strip().split('\n\n')
        self.ranges_dict = {}
        for value_range in ranges.split('\n'):
            key, _, values = value_range.partition(': ')
            self.ranges_dict[key] = tuple(map(lambda x: tuple(map(int,x.split('-'))), values.split(' or ')))
        tickets = [list(map(int, ticket.split(','))) for ticket in other_tickets.split('\n')[1:]]
        inv_tickets = partial(invalid_numbers_sum, ranges=self.ranges_dict)
        return sum(map(inv_tickets, tickets))


DayPart1()


def guess_fields(tickets, ranges_dict):
    guessed_fields = defaultdict(list)

    for i, values in enumerate(zip(*tickets)):
        for field, ranges in ranges_dict.items():
            if all(any(r_min <= value <= r_max for r_min, r_max in ranges) for value in values):
                guessed_fields[i].append(field)
    while not all(len(field) == 1 for idx, field in guessed_fields.items()):
        singles = {idx: fields[0] for idx, fields in guessed_fields.items() if len(fields) == 1}
        for idx, fields in guessed_fields.items():
            if len(fields)>1:
                for fvalue in fields.copy():
                    if fvalue in singles.values():
                        fields.remove(fvalue)

    return guessed_fields


class DayPart2(AoCFramework):
    test_cases = [
        ('''departure class: 0-1 or 4-19
departure row: 0-5 or 8-19
departure seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9''', 1716),
    ]
    known_result = 2587271823407

    def go(self):
        raw = self.puzzle_input
        ranges, my_ticket, other_tickets = raw.strip().split('\n\n')
        my_ticket = list(map(int, my_ticket.split('\n')[1].split(',')))
        self.ranges_dict = {}
        for value_range in ranges.split('\n'):
            key, _, values = value_range.partition(': ')
            self.ranges_dict[key] = tuple(map(lambda x: tuple(map(int, x.split('-'))), values.split(' or ')))
        tickets = [list(map(int, ticket.split(','))) for ticket in other_tickets.split('\n')[1:]]
        inv_tickets = partial(invalid_numbers, ranges=self.ranges_dict)

        valid_tickets = list(filter(lambda x: inv_tickets(x) == 0, tickets))
        guessed_fields = [value[0] for _, value in sorted(tuple(guess_fields(valid_tickets, self.ranges_dict).items()))]
        prod = 1
        for i, field in enumerate(guessed_fields):
            if field.startswith('departure'):
                prod *= my_ticket[i]
        return prod


DayPart2()
