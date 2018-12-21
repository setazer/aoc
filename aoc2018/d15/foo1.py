import sys
from operator import itemgetter, attrgetter

from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('''#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######''',27730),
        ('''#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######''',36334),
        ('''#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######''',39514),
        ('''#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######''',27755),
        ('''#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######''',28944),
        ('''#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########''',18740),
    )
#     test_cases=(('''#########
# #G..G..G#
# #.......#
# #.......#
# #G..E..G#
# #.......#
# #.......#
# #G..G..G#
# #########''',999),)
    def go(self):
        class NoEnemiesLeft(Exception):
            pass
        raw = self.raw_puzzle_input.rstrip()
        raw_split = self.linesplitted
        walls = []
        units = []

        def draw_field(i,just_print=False,current_coords=None,final=False):
            max_y = max(walls, key=itemgetter(1))[1]
            max_x = max(walls, key=itemgetter(0))[0]
            field = ''
            unit_positions={(unit.x,unit.y):unit for unit in units}
            for y in range(max_y+1):
                line = ''
                for x in range(max_x+1):
                    if (x, y) in walls:
                        line += '#'
                    elif current_coords and (x,y) == current_coords:
                        line+='+'
                    elif (x, y) in unit_positions and isinstance(unit_positions[(x,y)],Elf):
                        line += 'E'
                    elif (x, y) in unit_positions and isinstance(unit_positions[(x, y)], Goblin):
                        line += 'G'
                    else:
                        line += '.'
                field += f"{line}\n"
            units_for_movement = sorted(units, key=attrgetter('y', 'x'))
            field += "\n".join(map(str,units_for_movement))
            if just_print:
                print(field)
            else:
                filename=f'field{i}.txt' if not final else f'field{i}_f.txt'
                with open(filename, 'w') as field_file:
                    field_file.write(field)
        pathfinder_directions = ((0,-1),(-1,0),(1,0),(0,1))
        def pos_add(pos_tuple,rel_pos_tuple):
            return tuple(x + y for x, y in zip(pos_tuple, rel_pos_tuple))
        def invert_tuple(pos_tuple):
            return tuple(-x for x in pos_tuple)
        class Unit():
            def __init__(self,x,y):
                self.x,self.y=x,y
                self.hp = 200
                self.damage = 3
                self.neighbors={(0,-1):None,(-1,0):None,(1,0):None,(0,1):None}
            def scan_neighbors(self):
                units_positions = {(unit.x,unit.y):unit for unit in units}
                for neighbor in self.neighbors:
                    rel_pos = pos_add((self.x, self.y), neighbor)
                    if rel_pos in units_positions:
                        self.neighbors[neighbor]=units_positions[rel_pos]
                        units_positions[rel_pos].neighbors[invert_tuple(neighbor)]=self
                    else:
                        self.neighbors[neighbor]=None
            def draw_field_and_paths(self,paths):
                max_y = max(walls, key=itemgetter(1))[1]
                max_x = max(walls, key=itemgetter(0))[0]
                field = ''
                unit_positions = {(unit.x, unit.y): unit for unit in units}
                for y in range(max_y + 1):
                    line = ''
                    for x in range(max_x + 1):
                        if (x, y) in walls:
                            line += '#'
                        elif (x, y) in unit_positions and isinstance(unit_positions[(x, y)], Elf):
                            line += 'E'
                        elif (x, y) in unit_positions and isinstance(unit_positions[(x, y)], Goblin):
                            line += 'G'
                        elif (x, y) in paths:
                            line += str(paths[(x, y)]%10)
                        else:
                            line += '.'
                    field += f"{line}\n"
                print(field)
            def move(self):
                self.scan_neighbors()
                for neighbor in self.neighbors.values():
                    if neighbor and not isinstance(neighbor,self.__class__):
                        return
                enemies = [unit for unit in units if not isinstance(unit,self.__class__)]
                if not enemies:
                    raise NoEnemiesLeft
                accessible_enemies={(unit.x,unit.y):unit for unit in units if not isinstance(unit,self.__class__) and not all(unit.neighbors.values())}
                friends={(unit.x,unit.y):unit for unit in units if isinstance(unit,self.__class__)}
                attackable_points = {pos_add((unit.x,unit.y),neighbor_rel_pos):unit for unit in accessible_enemies.values() for neighbor_rel_pos in unit.neighbors if not unit.neighbors[neighbor_rel_pos]}
                if not accessible_enemies:
                    return
                # sorted_distances = min(((unit,distance,unit.x,unit.y) for unit,distance in enemy_distances.items()),key=(itemgetter(1),itemgetter(0).x,itemgetter(0).y))
                # spawn pathfinder
                paths={}
                path_edges = [(self.x,self.y)]
                for i in range(1,51):
                    new_path_edges = []
                    for edge in path_edges:
                        for direction in pathfinder_directions:
                            cur_pos=pos_add(edge,direction)
                            if cur_pos in walls or cur_pos in friends:
                                continue
                            else:
                                if not cur_pos in new_path_edges and not cur_pos in paths:
                                    paths.setdefault(cur_pos,i)
                                    new_path_edges.append(cur_pos)

                    path_edges=new_path_edges
                    if not path_edges:
                        break
                # get path
                closest_attackable_points=[]

                for pos,enemy in accessible_enemies.items():
                    accessible_points = list((unit,paths[unit_pos],*unit_pos) for unit_pos,unit in attackable_points.items() if unit==enemy and unit_pos in paths)
                    if accessible_points:
                        closest_attackable_point = min(accessible_points,key=itemgetter(1,3,2))
                        closest_attackable_points.append(closest_attackable_point)
                if closest_attackable_points:
                    target_destination=min(closest_attackable_points,key=itemgetter(1,3,2))
                    target_range,target_point = target_destination[1],(target_destination[2],target_destination[3])
                    for i in range(target_range,0,-1):
                        for direction in (pathfinder_directions):
                            rel_pos=pos_add(target_point,direction)
                            if paths.get(rel_pos,999)<i:
                                target_point=rel_pos
                                break
                    self.x,self.y=target_point
                    self.scan_neighbors()
            def attack(self):
                if self.hp<=0:
                    return
                targets = []
                for pos,neighbor in self.neighbors.items():
                    if neighbor and not isinstance(neighbor,self.__class__) and neighbor.hp>0:
                        targets.append((neighbor,neighbor.hp,*pos))
                if targets:
                    target_to_attack = min(targets,key=itemgetter(1,3,2))
                    target_to_attack[0].hp-=self.damage
                    if target_to_attack[0].hp<=0:
                        units.remove(target_to_attack[0])
                        self.neighbors[(target_to_attack[2],target_to_attack[3])]=None





        class Goblin(Unit):
            def __repr__(self):
                return f"Goblin[{self.hp}] @ ({self.x},{self.y})"
        class Elf(Unit):
            def __repr__(self):
                return f"Elf[{self.hp}] @ ({self.x},{self.y})"

        for y,row in enumerate(raw_split):
            for x,char in enumerate(row):
                if char=='#':
                    walls.append((x,y))
                elif char=='G':
                    units.append(Goblin(x,y))
                elif char=='E':
                    units.append(Elf(x,y))
        i=0
        draw_field(i)
        try:
            while True:
                units_for_movement = sorted(units,key=attrgetter('y','x'))
                for unit in units_for_movement:
                    if unit.hp>0:
                        unit.move()
                        unit.attack()

                i += 1
                draw_field(i)
        except NoEnemiesLeft:
            pass
        total_hp = sum(unit.hp for unit in units)
        print(f"{i} * {total_hp}")
        return total_hp*i



Day()