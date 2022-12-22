import itertools
import operator
import re

from aocframework import AoCFramework



class DayPart1(AoCFramework):
    test_cases = (
        ("""root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32""", 152),
    )
    known_result = None

    def go(self):
        op_monkeys = {}
        num_monkeys = {}
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }
        for monkey in self.linesplitted:
            monkey_name, _, monkey_yell = monkey.partition(': ')
            try:
                num_monkeys[monkey_name] = int(monkey_yell)
            except ValueError:
                monkey1, op, monkey2 = monkey_yell.split(' ')
                op_monkeys[monkey_name] = (monkey1, ops[op], monkey2)

        while True:
            for op_monkey_name, op_monkey_yell in op_monkeys.copy().items():
                monkey1, op, monkey2 = op_monkey_yell
                if monkey1 in num_monkeys and monkey2 in num_monkeys:
                    num_monkeys[op_monkey_name] = op(num_monkeys[monkey1], num_monkeys[monkey2])
                    del op_monkeys[op_monkey_name]
            if 'root' in num_monkeys:
                break
        return num_monkeys['root']


DayPart1()

def build_equation(op_monkeys, num_monkeys):
    old_equation = None
    new_equation = op_monkeys.pop('root')
    while old_equation != new_equation:
        old_equation = new_equation
        for op_monkey, op_monkey_yell in op_monkeys.items():
            new_equation = new_equation.replace(op_monkey, f'({op_monkey_yell})')

    old_equation = None
    while old_equation != new_equation:
        old_equation = new_equation
        for num_monkey, num_monkey_yell in num_monkeys.items():
            new_equation = new_equation.replace(num_monkey, f'{num_monkey_yell}')

    return new_equation

re_expr = re.compile(r"(\((?P<num1>\d+) . (?P<num2>\d+)\))")

re_unknown_left = re.compile(r"\((?P<unknown>\(.*\)) (?P<op>.) (?P<num>\d+)\)")
re_unknown_right = re.compile(r"\((?P<num>\d+) (?P<op>.) (?P<unknown>\(.*\))\)")

re_final_left = re.compile(r"\((?P<unknown>.*) (?P<op>.) (?P<num>\d+)\)")
re_final_right = re.compile(r"\((?P<num>\d+) (?P<op>.) (?P<unknown>.*)\)")

def simplify_expression(expr):
    while found_expr := re_expr.search(expr):
        value = eval(found_expr.group(0))
        expr = expr[:found_expr.span(0)[0]] + str(int(value)) + expr[found_expr.span(0)[1]:]
    return expr


def get_answer(unwrapping, answer):
    ops = {
        '/': operator.mul,
        '*': operator.floordiv,
        '-': operator.add,
        '+': operator.sub,
    }
    right_ops = {
        '/': lambda x, y: y // x,
        '*': lambda x, y: x // y,
        '-': lambda x, y: y - x,
        '+': lambda x, y: x - y,
    }
    while True:
        left_match = re_unknown_left.match(unwrapping)
        if left_match:
            unwrapping = left_match.group('unknown')
            op = ops[left_match.group('op')]
            num = int(left_match.group('num'))
            answer = op(answer, num)
        right_match = re_unknown_right.match(unwrapping)
        if right_match:
            unwrapping = right_match.group('unknown')
            op = right_ops[right_match.group('op')]
            num = int(right_match.group('num'))
            answer = op(answer, num)

        if not left_match and not right_match:
            break
    final_left_match = re_final_left.match(unwrapping)
    if final_left_match:
        op = ops[final_left_match.group('op')]
        num = int(final_left_match.group('num'))
        answer = op(answer, num)
        return answer

    final_right_match = re_final_right.match(unwrapping)
    if final_right_match:
        op = right_ops[final_right_match.group('op')]
        num = int(final_right_match.group('num'))
        answer = op(answer, num)
        return answer
    return None


class DayPart2(AoCFramework):
    test_cases = (
        ("""root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32""", 301),
    )
    known_result = None

    def go(self):
        op_monkeys = {}
        num_monkeys = {}
        for monkey in self.linesplitted:
            monkey_name, _, monkey_yell = monkey.partition(': ')
            try:
                num_monkeys[monkey_name] = int(monkey_yell)
            except ValueError:
                if monkey_name == 'root':
                    monkey_yell=monkey_yell.replace('+', '==')
                op_monkeys[monkey_name] = monkey_yell
        num_monkeys.pop('humn')

        eq = build_equation(op_monkeys, num_monkeys)
        eq = simplify_expression(eq)

        left_side, _, right_side = eq.partition(' == ')
        if 'humn' in left_side:
            return get_answer(left_side, int(right_side))
        else:
            return get_answer(right_side, int(left_side))


DayPart2()
