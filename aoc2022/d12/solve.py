import time

from aocframework import AoCFramework
from graph_stuff import Graph, parse_field


class DayPart1(AoCFramework):
    test_cases = (
        ('''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi''', 31),
    )
    known_result = None

    def go(self):
        raw = self.raw_puzzle_input
        field, adj_data, start, end = parse_field(raw.strip())
        graph = Graph(field, adj_data)
        shortest_path = graph.a_star_algorithm(start, end)
        return len(shortest_path) - 1


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi''', 29),
    )
    known_result = None

    def go(self):
        start_time = time.perf_counter()
        raw = self.raw_puzzle_input
        field, adj_data, start, end = parse_field(raw.strip())
        graph = Graph(field, adj_data)
        distances = {}
        for pos, char in field.items():
            if char not in 'Sa':
                continue
            path = graph.a_star_algorithm(pos, end)
            if not path:
                continue
            dist = len(path) - 1
            distances[pos] = dist
        result = min(distances.values())
        print(time.perf_counter() - start_time)
        return result


DayPart2()
