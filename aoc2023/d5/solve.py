from itertools import islice

from aocframework import AoCFramework


def batched(iterable, n):
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch


class Range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"Range({self.start}:{self.end})"

    def __hash__(self):
        return hash((self.start, self.end))

    def intersection(self, other):
        if not isinstance(other, Range):
            raise TypeError()

        if other in self:
            return other
        if self in other:
            return self

        if self.end < other.start or self.start > other.end:
            return None

        if self.start < other.start:
            new_start = self.start
        else:
            new_start = other.start

        if self.end > other.end:
            new_end = self.end
        else:
            new_end = other.end
        return Range(new_start, new_end)

    def __len__(self):
        return self.end - self.start + 1

    def __contains__(self, other):
        if isinstance(other, int):
            return self.start <= other <= self.end
        if isinstance(other, Range):
            return self.start <= other.start and self.end >= other.end
        raise TypeError()

    def copy(self):
        return Range(self.start, self.end)


class Transformer:
    def __init__(self, source_range: Range, destination_range: Range):
        self.source_range = source_range
        self.destination_range = destination_range

    def __repr__(self):
        return f"Transformer({self.source_range} to {self.destination_range})"

    @classmethod
    def from_string(cls, range_string):
        dest, src, size = range_string.strip().split(' ')
        src_range = Range(int(src), int(src)+int(size)-1)
        dest_range = Range(int(dest), int(dest)+int(size)-1)
        return cls(src_range, dest_range)

    def transform(self, source_number):
        if source_number < self.source_range.start or source_number > self.source_range.end:
            return source_number
        offset = source_number - self.source_range.start
        return self.destination_range.start + offset

    def transform_range(self, src):
        start_offset = src.start - self.source_range.start
        end_offset = src.end - self.source_range.start
        return Range(self.destination_range.start + start_offset, self.destination_range.start + end_offset)


    def __contains__(self, item):
        return item in self.source_range


class DayPart1(AoCFramework):
    test_cases = (
        ('''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4''', 35),
    )
    known_result = 462648396

    def go(self):
        raw = self.raw_puzzle_input.strip()
        seeds_and_maps = raw.split('\n\n')
        seeds = [int(item) for item in seeds_and_maps[0].strip().partition(': ')[-1].split(' ')]
        stages = {seed: 'seed' for seed in seeds}
        result = {seed: seed for seed in seeds}
        maps = {}
        history = {seed: [('seed', seed)] for seed in seeds}
        for convertion_map in seeds_and_maps[1:]:
            map_data = convertion_map.split('\n')
            name = map_data[0].partition(' ')[0]
            from_conv, _, to_conv = name.partition('-to-')
            ranges = [Transformer.from_string(line) for line in map_data[1:]]
            maps[from_conv] = (to_conv, ranges)
        while any(value != 'location' for value in stages.values()):
            for seed, stage in stages.items():
                dest, ranges = maps[stage]
                seed_value = result[seed]
                for conv_range in ranges:
                    if seed_value in conv_range:
                        result[seed] = conv_range.transform(seed_value)
                        break
                stages[seed] = dest
                history[seed].append((dest, result[seed]))
        return min(result.values())


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4''', 46),
    )
    known_result = 2520479

    def transform_range(self, stage, dest, transformers, seed_range):
        result = set()
        stack = set([(stage, seed_range)])
        while stack:
            stage, seed_range = stack.pop()
            if stage == dest:
                result.add(seed_range)
                continue
            transformers_hit = False
            for transformer in transformers:
                if transformers_hit:
                    break
                inter = seed_range.intersection(transformer.source_range)
                if inter is None:
                    continue
                elif inter is seed_range:
                    stack.add((dest, transformer.transform_range(seed_range)))
                    transformers_hit = True
                elif inter is transformer.source_range:
                    stack.update((
                        (stage, Range(seed_range.start, transformer.source_range.start-1)),
                        (stage, Range(transformer.source_range.end+1, seed_range.end)),
                        (dest, transformer.destination_range.copy()),
                    ))
                    transformers_hit = True

                else:
                    if seed_range.start > transformer.source_range.start:
                        stack.update((
                            (dest, transformer.transform_range(Range(seed_range.start, transformer.source_range.end))),
                            (stage, Range(transformer.source_range.end+1, seed_range.end)),
                        ))
                        transformers_hit = True

                    else:
                        stack.update((
                            (stage, Range(seed_range.start, transformer.source_range.start-1)),
                            (dest, transformer.transform_range(Range(transformer.source_range.start, seed_range.end))),
                        ))
                        transformers_hit = True

            if not transformers_hit:
                result.add(seed_range)
        return result

    def go(self):
        raw = self.raw_puzzle_input.strip()
        seeds_and_maps = raw.split('\n\n')
        seeds = [Range(int(start), int(start)+int(size)-1) for start, size in batched(seeds_and_maps[0].strip().partition(': ')[-1].split(' '), 2)]
        stages = ['seed'] * len(seeds)
        result = [{seed} for seed in seeds]
        maps = {}
        for convertion_map in seeds_and_maps[1:]:
            map_data = convertion_map.split('\n')
            name = map_data[0].partition(' ')[0]
            from_conv, _, to_conv = name.partition('-to-')
            transformers = [Transformer.from_string(line) for line in map_data[1:]]
            maps[from_conv] = (to_conv, transformers)

        while any(value != 'location' for value in stages):
            for i, stage in enumerate(stages):
                dest, transformers = maps[stage]
                seeds_ranges = result[i]
                transformed_ranges=set()
                for seed_range in seeds_ranges.copy():
                    transformed_ranges.update(self.transform_range(stage, dest, transformers, seed_range))
                result[i] = transformed_ranges
                stages[i] = dest

        return min(res_range.start for res_ranges in result for res_range in res_ranges)


DayPart2()
