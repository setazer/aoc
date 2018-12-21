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
        with open('field0.txt', 'w') as field_file:
            for cell_y in range(50):
                for cell_x in range(50):
                    field_file.write(field[(cell_x, cell_y)])
                field_file.write('\n')

        for i in range(10):
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
            with open(f'field{i+1}.txt','w') as field_file:
                for cell_y in range(50):
                    for cell_x in range(50):
                        field_file.write(field[(cell_x,cell_y)])
                    field_file.write('\n')
        cnt_field = Counter(field.values())
        trees,lumberyards = cnt_field['|'],cnt_field['#']
        return trees*lumberyards








Day()