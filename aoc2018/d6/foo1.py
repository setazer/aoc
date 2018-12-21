from collections import defaultdict
from operator import itemgetter

from aocframework import AoCFramework

def tree(): return defaultdict(tree)

class Day(AoCFramework):
    test_cases = ()

    def go(self):
        raw = self.raw_puzzle_input
        raw_split = self.linesplitted
        def manhattan_distance(point,target_poing):
            return abs(target_poing[0] - point[0]) + abs(target_poing[1]-point[1])
        points = {n:tuple(map(int,line.split(', '))) for n,line in enumerate(raw_split)}
        field_min_x = min(points.values(),key=itemgetter(0))[0]
        field_min_y = min(points.values(),key=itemgetter(1))[1]
        field_max_x = max(points.values(),key=itemgetter(0))[0]
        field_max_y = max(points.values(),key=itemgetter(1))[1]
        distances = tree()
        for point,coords in points.items():
            for x in range(field_min_x-1,field_max_x+2):
                for y in range(field_min_y-1,field_max_y+2):
                    distances[(x,y)][point] = manhattan_distance((x,y),coords)
        field = {}
        for x in range(field_min_x - 1, field_max_x + 2):
            for y in range(field_min_y - 1, field_max_y + 2):
                min_dist = min(distances[(x,y)].values())
                min_dist_elems = [item for item,value in distances[(x,y)].items() if value == min_dist]
                field[(x,y)]= '.' if len(min_dist_elems)>1 else min_dist_elems[0]
                print(field[(x,y)],end=' ')
            print()
        edges = {field[(x,y)] for x in range(field_min_x - 1, field_max_x + 2) for y in range(field_min_y - 1, field_max_y + 2)
                 if not ( field_min_x <= x <=field_max_x and field_min_y <= y <= field_max_y)}
        filtered_field = list(filter(lambda key: key not in edges,field.values()))
        filtered_field_counts = {item:filtered_field.count(item) for item in filtered_field}
        return max(filtered_field_counts.values())

Day()