import re
from typing import Union

from aocframework import AoCFramework


RE_OP = re.compile(r'Operation: new = old (?P<op>\W) (?P<num>\d+)')
RE_NUMBER = re.compile(r'(\d+)')


class Monke:
    def __init__(self, items, op, inspection, true_monke, false_monke):
        self.items: list = items
        self.op = op
        self.inspect_number = inspection
        self.true_monke: Union[str, Monke] = true_monke
        self.false_monke: Union[str, Monke] = false_monke
        self.inspections = 0

    def __repr__(self):
        return f"Monke(throws:{self.inspections}, items: {self.items})"

    @classmethod
    def from_data(cls, monke_data):
        _, items_data, op_data, test_data, true_data, false_data = monke_data.split('\n')
        items = [int(item) for item in RE_NUMBER.findall(items_data)]

        operation = op_data.partition('= ')[-1]
        op = lambda old: eval(operation.replace('old', str(old)))

        test_num = int(RE_NUMBER.search(test_data).group(1))
        inspection = test_num

        true_monke = int(RE_NUMBER.search(true_data).group(1))
        false_monke = int(RE_NUMBER.search(false_data).group(1))
        return cls(items, op, inspection, true_monke, false_monke)

    def post_init(self, monkeys):
        self.true_monke = monkeys[self.true_monke]
        self.false_monke = monkeys[self.false_monke]

    def catch_item(self, item):
        self.items.append(item)

    def throw_item(self, item, monke):
        monke.catch_item(item)

    def business(self):
        while True:
            try:
                item = self.items.pop(0)
            except IndexError:  # mt
                return
            worry_level = self.op(item) // 3
            if (worry_level % self.inspect_number) == 0:
                self.throw_item(worry_level, self.true_monke)
            else:
                self.throw_item(worry_level, self.false_monke)
            self.inspections += 1

    def business_uncontrollable(self, nok):
        while True:
            try:
                item = self.items.pop(0)
            except IndexError:  # mt
                return
            worry_level = self.op(item)
            div, mod = divmod(worry_level, self.inspect_number)
            if mod == 0:
                self.throw_item(worry_level, self.true_monke)
            else:
                self.throw_item(worry_level % nok, self.false_monke)
            self.inspections += 1



class DayPart1(AoCFramework):
    test_cases = (
        ('''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
''', 10605),
    )
    known_result = 56595

    def go(self):
        monkeys = []
        for monke_data in self.raw_puzzle_input.strip().split('\n\n'):
            monkeys.append(Monke.from_data(monke_data))
        for monke in monkeys:
            monke.post_init(monkeys)

        for _ in range(20):
            for monke in monkeys:
                monke.business()
        top_monkeys = sorted(monkeys, key=lambda m: m.inspections, reverse=True)
        return top_monkeys[0].inspections * top_monkeys[1].inspections


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        (
            '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
''', 2713310158),
    )
    known_result = None

    def go(self):
        monkeys = []
        for monke_data in self.raw_puzzle_input.strip().split('\n\n'):
            monkeys.append(Monke.from_data(monke_data))
        for monke in monkeys:
            monke.post_init(monkeys)
        total_inspect_product = 1
        for monke in monkeys:
            total_inspect_product *= monke.inspect_number
        for business_round in range(1, 10001):

            for monke in monkeys:
                monke.business_uncontrollable(total_inspect_product)
            if business_round in (1, 20) or business_round % 1000 == 0:
                print("ROUND:", business_round, "Monkeys:", monkeys, sep=' ')
        top_monkeys = sorted(monkeys, key=lambda m: m.inspections, reverse=True)
        return top_monkeys[0].inspections * top_monkeys[1].inspections


DayPart2()
