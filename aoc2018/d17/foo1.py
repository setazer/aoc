from collections import deque
from copy import copy
from operator import itemgetter

from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (('''x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504''',57),)

    def go(self):
        raw = self.raw_puzzle_input.rstrip()
        raw_split = self.linesplitted
        clay_spots = set()
        for clay_def in raw_split:
            static_pos, dynamic_pos = clay_def.split(', ')
            coord1, coord1_val = static_pos.split('=')
            coord2, coord2_vals = dynamic_pos.split('=')
            coord2_val1, coord2_val2 = coord2_vals.split('..')
            coord1_val, coord2_val1, coord2_val2 = map(int, [coord1_val, coord2_val1, coord2_val2])
            if coord1 == 'x':
                for y in range(coord2_val1, coord2_val2 + 1):
                    clay_spots.add((coord1_val, y))
            elif coord1 == 'y':
                for x in range(coord2_val1, coord2_val2 + 1):
                    clay_spots.add((x, coord1_val))
        min_y = min(clay_spots,key=itemgetter(1))[1]
        max_y = max(clay_spots,key=itemgetter(1))[1]
        # min_x = min(clay_spots, key=itemgetter(0))[0]
        # max_x = max(clay_spots, key=itemgetter(0))[0]
        # with open('field.txt','w') as field:
        #     for y in range(min_y,max_y+1):
        #         line = ''
        #         for x in range(min_x,max_x+1):
        #             line+=('#' if (x,y) in clay_spots else '.')
        #         field.write(f'{line}\n')
        water = set()
        water_positions={}
        def is_solid(instance):
            return instance == 'clay' or isinstance(instance, WaterDrop) and instance.is_settled
        class WaterDrop():
            def __init__(self, x, y):
                self.x = x
                self.y = y
                if (self.x,self.y) in water_positions:
                    print(i,'OVERLAPPING DETECTED')
                self.neighbors = {'left': None, 'down': None, 'right': None, 'up':None}
                self.is_settled=False
                self.at_bottom=False
                self.need_update=True

            def __repr__(self):
                return f"Water drop @ {self.x},{self.y}"

            def scan_surroundings(self):
                if self.y==max_y:
                    self.at_bottom=True
                self.neighbors['right'],self.neighbors['left'],self.neighbors['down'] =  ('clay' if pos in clay_spots else None for pos in [(self.x + 1, self.y),(self.x - 1, self.y),(self.x, self.y + 1)])
                self.neighbors['right'] = water_positions.get((self.x + 1, self.y),self.neighbors['right'])
                self.neighbors['left'] = water_positions.get((self.x - 1, self.y),self.neighbors['left'])
                self.neighbors['down'] = water_positions.get((self.x, self.y + 1),self.neighbors['down'])
                self.neighbors['up'] = water_positions.get((self.x, self.y -1), self.neighbors['up'])

            def settle(self, direction):
                if direction in ['left','right']:
                    chain_of_water = [self]
                    current_neighbor = self.neighbors[direction]
                    while True:
                        if not current_neighbor:
                            chain_of_water=[]
                            break
                        if current_neighbor=='clay':
                            break
                        else:
                            chain_of_water.append(current_neighbor)
                            current_neighbor.scan_surroundings()
                            current_neighbor = current_neighbor.neighbors[direction]

                    for water_drop in chain_of_water:
                        if water_drop.neighbors.get('up'):
                            water_drop.neighbors['up'].need_update=True
                        water_drop.is_settled = True
                        water_drop.need_update=False

                elif direction == 'both':
                    chain_of_water = deque([self])
                    left_neighbor = self.neighbors['left']
                    right_neighbor=self.neighbors['right']
                    left_corner = right_corner = False
                    while True:
                        if left_neighbor=='clay':
                            left_corner=True
                        if right_neighbor == 'clay':
                            right_corner=True
                        if isinstance(left_neighbor,WaterDrop):
                            chain_of_water.appendleft(left_neighbor)
                            left_neighbor.scan_surroundings()
                            left_neighbor=left_neighbor.neighbors['left']
                        if isinstance(right_neighbor,WaterDrop):
                            chain_of_water.append(right_neighbor)
                            right_neighbor.scan_surroundings()
                            right_neighbor=right_neighbor.neighbors['right']
                        if left_corner and right_corner or left_corner and not right_neighbor or not left_neighbor and right_corner or not(left_neighbor or right_neighbor):
                            break
                    if left_corner and right_corner:
                        for drop in chain_of_water:
                            drop.is_settled=True
                            drop.need_update=False
                            if drop.neighbors.get('up'):
                                drop.neighbors['up'].need_update = True



            def spawn_new(self):
                if self.is_settled or self.at_bottom:
                    self.need_update=False
                    return
                if not self.need_update:
                    return
                if not self.neighbors['down']:
                    if (self.x, self.y + 1) not in water_positions:
                        new_water_drop = WaterDrop(self.x, self.y + 1)
                        new_water_drop.scan_surroundings()
                        new_water_drop.neighbors['up'] = self
                        self.neighbors['down'] = new_water_drop
                        water.add(new_water_drop)
                        water_positions[(self.x, self.y + 1)]=new_water_drop
                    else:
                        self.neighbors['down'] = water_positions[(self.x, self.y+1)]
                elif not self.neighbors['left'] and not self.neighbors['right'] and is_solid(self.neighbors['down']):
                    if (self.x - 1, self.y) not in water_positions:
                        new_water_drop = WaterDrop(self.x - 1, self.y)
                        new_water_drop.scan_surroundings()
                        new_water_drop.neighbors['right'] = self
                        self.neighbors['left'] = new_water_drop
                        water.add(new_water_drop)
                        water_positions[(self.x - 1, self.y)] = new_water_drop
                    else:
                        self.neighbors['left'] = water_positions[(self.x - 1, self.y)]
                    if (self.x + 1, self.y) not in water_positions:
                        new_water_drop = WaterDrop(self.x + 1, self.y)
                        new_water_drop.scan_surroundings()
                        new_water_drop.neighbors['left'] = self
                        self.neighbors['right'] = new_water_drop
                        water.add(new_water_drop)
                        water_positions[(self.x + 1, self.y)] = new_water_drop
                    else:
                        self.neighbors['right'] = water_positions[(self.x + 1, self.y)]
                elif not self.neighbors['left'] and is_solid(self.neighbors['down']):
                    if (self.x - 1, self.y) not in water_positions:
                        new_water_drop = WaterDrop(self.x - 1, self.y)
                        new_water_drop.scan_surroundings()
                        new_water_drop.neighbors['right'] = self
                        self.neighbors['left'] = new_water_drop
                        water.add(new_water_drop)
                        water_positions[(self.x - 1, self.y)] = new_water_drop
                    else:
                        self.neighbors['left'] = water_positions[(self.x - 1, self.y)]
                elif not self.neighbors['right'] and is_solid(self.neighbors['down']):
                    if (self.x + 1, self.y) not in water_positions:
                        new_water_drop = WaterDrop(self.x + 1, self.y)
                        new_water_drop.scan_surroundings()
                        new_water_drop.neighbors['left'] = self
                        self.neighbors['right'] = new_water_drop
                        water.add(new_water_drop)
                        water_positions[(self.x + 1, self.y)] = new_water_drop
                    else:
                        self.neighbors['right'] = water_positions[(self.x + 1, self.y)]
                elif self.neighbors['left'] and self.neighbors['down'] and self.neighbors['right']:
                    if is_solid(self.neighbors['left']) and is_solid(self.neighbors['down']):
                        self.settle('right')
                    elif is_solid(self.neighbors['right']) and is_solid(self.neighbors['down']):
                        self.settle('left')
                    elif is_solid(self.neighbors['down']):
                        self.settle('both')
                self.need_update = False

        def draw_field(i,partial=True):
            water_updated = set((drop.x, drop.y) for drop in water if drop.need_update)
            water_settled = set((drop.x, drop.y) for drop in water if drop.is_settled)
            min_y = min(water_positions, key=itemgetter(1))[1]
            max_y = max(water_positions, key=itemgetter(1))[1]
            min_x = min(water_positions, key=itemgetter(0))[0]
            max_x = max(water_positions, key=itemgetter(0))[0]
            field = ''
            if partial:
                y_from=max_y - 50
            else:
                y_from=min_y - 1
            for y in range(max(0, y_from), max_y + 2):
                line = ''
                for x in range(max(0, min_x - 1), max_x + 2):
                    if (x, y) in clay_spots:
                        line += '#'
                    elif (x, y) in water_updated:
                        line += 'X'
                    elif (x, y) in water_settled:
                        line += '~'
                    elif (x, y) in water_positions:
                        line += '|'
                    else:
                        line += '.'
                field += f"{line}\n"
            with open(f'field{i}.txt', 'w') as field_file:
                field_file.write(field)

        initial_drop = WaterDrop(500, 0)
        initial_drop.scan_surroundings()
        water.add(initial_drop)
        water_positions[(500,0)]=initial_drop
        simulate = True
        i = 0
        check_stats=False
        while simulate:
            if any(drop.at_bottom for drop in water):
                check_stats=True
            if check_stats:
                water_status = deque(drop.is_settled for drop in water)
                total,settled = len(water_status),sum(water_status)
            water_drops = set(drop for drop in water if drop.need_update)
            for water_drop in water_drops:
                water_drop.spawn_new()
            if not water_drops:
                print(i,'NO UPDATES LEFT!')
                draw_field(i)
                print('')
            if check_stats:
                water_status = deque(drop.is_settled for drop in water)
                total_new,settled_new=len(water_status),sum(water_status)
                if total==total_new and settled==settled_new and any(drop.at_bottom for drop in water):
                    simulate = False
            if i % 3000 == 0:
                draw_field(i)
            i += 1
        draw_field(i,False)
        counted_water=set(drop for drop in water if min_y<=drop.y<=max_y)
        return len(counted_water)


Day()
