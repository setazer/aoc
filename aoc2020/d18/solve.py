from functools import reduce

from aocframework import AoCFramework
import operator

OPERATOR_MAPPING = {
    '*': operator.mul,
    '+': operator.add,
}


def deparenthise(expr, eval_func):
    while '(' in expr:
        start = None
        for i, c in enumerate(expr):
            if c == '(':
                start = i
            elif c == ')':
                end = i
                expr = expr[:start]+str(eval_func(expr[start+1:end]))+expr[end+1:]
                break
    return expr


def calc(expr):
    expr = expr.replace(' ', '')
    operations, values = get_values_and_ops(expr)
    value = values[0]
    for op, y in zip(operations, values[1:]):
        value = op(value, y)
    return value


def get_values_and_ops(expr):
    values = []
    operations = []
    start = 0
    for i, c in enumerate(expr):
        if c in ('*', '+'):
            end = i
            values.append(int(expr[start:end]))
            operations.append(OPERATOR_MAPPING[c])
            start = end + 1
    else:
        values.append(int(expr[start:]))
    return operations, values


def calc_add_first(expr):
    expr = expr.replace(' ', '')
    operations, values = get_values_and_ops(expr)
    while operator.add in operations:
        for i, op in enumerate(operations):
            if op is operator.add:
                values[i] = op(values[i], values[i+1])
                values.pop(i+1)
                operations.pop(i)
                break
    value = values[0]
    for op, y in zip(operations, values[1:]):
        value = op(value, y)
    return value




class DayPart1(AoCFramework):
    test_cases = (
        ('1 + (2 * 3) + (4 * (5 + 6))', 51),
    )
    known_result = 8929569623593

    def go(self):
        raw_split = self.linesplitted
        results = []
        for line in raw_split:
            results.append(calc(deparenthise(line, calc)))
        return sum(results)


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('1 + (2 * 3) + (4 * (5 + 6))', 51),
        ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 669060),
    )
    known_result = 231235959382961

    def go(self):
        raw_split = self.linesplitted
        results = []
        for line in raw_split:
            results.append(calc_add_first(deparenthise(line, calc_add_first)))
        return sum(results)


DayPart2()
