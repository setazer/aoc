from collections import Counter
from copy import deepcopy

from aocframework import AoCFramework
from operator import attrgetter
class Day(AoCFramework):
    test_cases = ()
    def go(self):
        raw = self.puzzle_input.rstrip()
        raw_split = self.linesplitted
        field=[]

        class IntersectionTurns:
            LEFT=0
            STRAIGHT = 1
            RIGHT = 2
        class Directions:
            show={0:">",1:"^",2:"<",3:"v"}
            RIGHT = 0
            UP = 1
            LEFT = 2
            DOWN = 3
        class Tracks:
            HORIZONTAL = '-'
            VERTICAL = '|'
            DIAGONAL1='\\'
            DIAGONAL2='/'
            INTERSECTION = '+'

        class Cart:
            interturn=0
            pos = (0,0)
            dir = Directions.RIGHT
            crashed = False
            def __init__(self,pos,dir):
                self.pos=pos
                self.dir = dir

            def __repr__(self):
                return f"{Directions.show[self.dir]} @ {self.pos}"
            def turn_on_intersection(self):
                if self.interturn == IntersectionTurns.LEFT:
                    self.dir = (self.dir + 1) % 4
                    self.interturn = IntersectionTurns.STRAIGHT
                elif self.interturn == IntersectionTurns.STRAIGHT:
                    self.interturn = IntersectionTurns.RIGHT
                elif self.interturn == IntersectionTurns.RIGHT:
                    self.dir = (self.dir - 1) % 4
                    self.interturn = IntersectionTurns.LEFT

            def move(self):
                nonlocal field,carts
                x,y = self.pos
                if self.dir == Directions.RIGHT:
                    x+=1
                elif self.dir == Directions.UP:
                    y-=1
                elif self.dir == Directions.LEFT:
                    x-=1
                elif self.dir == Directions.DOWN:
                    y+=1
                self.pos = (x,y)
                if field[y][x]== Tracks.DIAGONAL1 and (self.dir==Directions.UP or self.dir==Directions.DOWN):
                    self.dir = (self.dir + 1) % 4
                elif field[y][x]== Tracks.DIAGONAL1 and (self.dir==Directions.RIGHT or self.dir==Directions.LEFT):
                    self.dir = (self.dir - 1) % 4
                elif field[y][x]== Tracks.DIAGONAL2 and (self.dir==Directions.UP or self.dir==Directions.DOWN):
                    self.dir = (self.dir - 1) % 4
                elif field[y][x]== Tracks.DIAGONAL2 and (self.dir==Directions.RIGHT or self.dir==Directions.LEFT):
                    self.dir = (self.dir + 1) % 4
                elif field[y][x]==Tracks.INTERSECTION:
                    self.turn_on_intersection()

        carts = set()
        # save field
        for row in raw_split:
            field.append(list(row))
        for y in range(len(field)):
            for x in range(len(field[0])):
                if field[y][x] == '^':
                    carts.add(Cart((x,y),Directions.UP))
                    field[y][x]='|'
                elif field[y][x] == 'v':
                    carts.add(Cart((x,y),Directions.DOWN))
                    field[y][x]='|'
                elif field[y][x] == '>':
                    carts.add(Cart((x, y), Directions.RIGHT))
                    field[y][x] = '-'
                elif field[y][x] == '<':
                    carts.add(Cart((x, y), Directions.LEFT))
                    field[y][x] = '-'

        def simulate(step):
            sorted_carts = sorted(carts,key=attrgetter('pos'))
            crashed_carts = []
            crashed = False
            for cart in sorted_carts:
                cart.move()
                cart_positions = Counter(cart.pos for cart in carts)
                if len(cart_positions.most_common()) != len(carts):
                    crashed_carts=[cart for cart in carts if cart.pos == cart_positions.most_common()[0][0]]
                    print(cart_positions.most_common()[0])
                    crashed = True
            for cart in crashed_carts:
                carts.remove(cart)
            if crashed:
                print(carts)

        for i in range(100000):
            # with open(f'frame{i}.txt','w') as frame:
            #     actual_field = deepcopy(field)
            #     for cart in carts:
            #         x,y = cart.pos
            #         if cart.dir == Directions.RIGHT:
            #             actual_field[y][x] = '>'
            #         elif cart.dir == Directions.LEFT:
            #             actual_field[y][x] = '<'
            #         elif cart.dir == Directions.UP:
            #             actual_field[y][x] = '^'
            #         elif cart.dir == Directions.DOWN:
            #             actual_field[y][x] = 'V'
            #     field_repr = '\n'.join(''.join(row) for row in actual_field)
            #     frame.write(field_repr)
            simulate(i)
            if len(carts)==1:
                print(carts)
                break

Day()
