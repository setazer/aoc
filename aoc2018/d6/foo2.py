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
        total_safe_region_size = 0
        for x in range(field_min_x, field_max_x + 1):
            for y in range(field_min_y, field_max_y + 1):
                total_point_distance = 0
                for point,coords in points.items():
                    point_distance = manhattan_distance((x,y),coords)
                    total_point_distance+=point_distance
                if total_point_distance<=10000:
                    total_safe_region_size+=1
        return total_safe_region_size



Day()