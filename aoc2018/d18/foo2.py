from collections import Counter
from copy import copy

from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = ()

    def go(self):
        raw = self.raw_puzzle_input.rstrip()
        raw_split = self.linesplitted
        field = {}
        for y,row in enumerate(raw_split):
            for x,char in enumerate(row):
                field[(x,y)]=char
        timeline = []
        dupe_values = {}
        for i in range(10000):
            timeline.append(field)
            new_field = copy(field)
            for cell_x in range(50):
                for cell_y in range(50):
                    cur_state = field[(cell_x,cell_y)]
                    trees = sum(1 for x in range(-1,2) for y in range(-1,2) if field.get((x+cell_x,y+cell_y),'.')=='|' and not (x==0 and y==0))
                    lumberyards = sum(1 for x in range(-1,2) for y in range(-1,2) if field.get((x+cell_x,y+cell_y),'.')=='#' and not (x==0 and y==0))
                    if cur_state=='.' and trees>2:
                        new_field[(cell_x,cell_y)]='|'
                    elif cur_state=='|' and lumberyards>2 :
                        new_field[(cell_x,cell_y)]='#'
                    elif cur_state=='#' and (lumberyards==0 or trees==0):
                        new_field[(cell_x, cell_y)] = '.'
            field=new_field
            if field in timeline:
                cnt_field = Counter(field.values())
                trees, lumberyards = cnt_field['|'], cnt_field['#']
                print(i,timeline.index(field))
                if not timeline.index(field) in dupe_values:
                    dupe_values[timeline.index(field)]=trees*lumberyards
                else:
                    break
        target_cycle=1000000000
        dupe_margin = max(dupe_values)-min(dupe_values)+1
        unrepeated_cycle = min(dupe_values)-1
        full_cycles = (target_cycle - unrepeated_cycle)//dupe_margin
        target_offset = target_cycle -(dupe_margin*full_cycles)
        return dupe_values[target_offset]








Day()