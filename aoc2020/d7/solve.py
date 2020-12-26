import re

from aocframework import AoCFramework

reg = re.compile(r"(\d+)\s(\w+\s\w+) bag")

def unpack(containers):

    for container, contents in containers.items():
        for i, (bag, amount) in enumerate(contents):
            if containers[bag] and bag != 'shiny gold':
                contents[i][0] = containers[bag]

def flatten_packs(container):
    new_contents = []
    for subcontainers, amount in container:
        if isinstance(subcontainers, list):
            new_contents.extend([[bag, subam*amount] for bag, subam in flatten_packs(subcontainers)])
        else:
            new_contents.append([subcontainers, amount])
    return new_contents

def flatten_packs_selfs(container):
    new_contents = []
    total = 0
    for subcontainers, amount in container:
        if isinstance(subcontainers, list):
            flattened, subtotal = flatten_packs_selfs(subcontainers)
            new_contents.extend([[bag, subam*amount] for bag, subam in flattened])
            total+=(subtotal*amount+amount)
        else:
            new_contents.append([subcontainers, amount])
            total+=amount
    return new_contents, total

class DayPart1(AoCFramework):
    test_cases = (
        ('''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.''', 4),
    )
    known_result = 337

    def go(self):
        raw_split = self.linesplitted
        containers = {}
        for line in raw_split:
            container, _, contents = line.partition(' bags contain ')
            containers[container] = [[cont, int(amounts)] for amounts, cont in reg.findall(contents)]
        unpack(containers)
        for container, contents in containers.items():
            containers[container] = flatten_packs(contents)
        return sum(['shiny gold' in sum(item, []) for item in containers.values()])


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.''', 126),
        ('''shiny gold bags contain 2 blue a bag, 3 red a bag
blue a bags contain 2 black a bags
red a bags contain 1 black a bags
black a bags contain nothing''', 12),
    )
    known_result = 50100

    def go(self):
        raw_split = self.linesplitted
        containers = {}
        for line in raw_split:
            container, _, contents = line.partition(' bags contain ')
            containers[container] = [[cont, int(amounts)] for amounts, cont in reg.findall(contents)]
        unpack(containers)
        _, total = flatten_packs_selfs(containers['shiny gold'])
        return total


DayPart2()
