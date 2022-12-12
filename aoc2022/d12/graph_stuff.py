from collections import namedtuple

vector = namedtuple('Vector', 'x, y')
neighbours = (vector(0, 1), vector(-1, 0), vector(0, -1), vector(1, 0))


def is_adjacent(char1, char2):
    char1 = char1.replace('S', 'a').replace('E', 'z')
    char2 = char2.replace('S', 'a').replace('E', 'z')
    pos1_val = ord(char1) - ord('a') + 1
    pos2_val = ord(char2) - ord('a') + 1
    return pos2_val < 2 + pos1_val


def parse_field(field_data):
    field = {}
    start = end = 0
    for y, row in enumerate(field_data.split('\n')):
        for x, char in enumerate(row):
            if char == 'S':
                start = (x, y)
            elif char == 'E':
                end = (x, y)
            field[(x, y)] = char

    adj_data = {}
    for pos, value in field.items():
        adj_list = []
        for offset in neighbours:
            x, y = pos
            n_pos = (x+offset.x, y+offset.y)
            neighbour_value = field.get(n_pos)
            if not neighbour_value:
                continue
            if is_adjacent(value, neighbour_value):
                adj_list.append((n_pos, 1))
        adj_data[pos] = adj_list

    return field, adj_data, start, end


class Graph:
    def __init__(self, field, adjac_lis, heur=lambda x: 1):
        self.field = field
        self.adjac_lis = adjac_lis
        self.heur = heur

    def get_neighbors(self, v):
        return self.adjac_lis[v]

    def a_star_algorithm(self, start, stop):
        # In this open_lst is a list of nodes which have been visited, but who's
        # neighbours haven't all been always inspected, It starts off with the start node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been always inspected
        open_lst = {start}
        closed_lst = set()

        # poo has present distances from start to all other nodes
        # the default value is +infinity
        poo = {}
        poo[start] = 0

        # par contains an adjac mapping of all nodes
        par = {}
        par[start] = start

        while len(open_lst) > 0:
            n = None

            # it will find a node with the lowest value of f() -
            for v in open_lst:
                if n == None or poo[v] + self.heur(v) < poo[n] + self.heur(n):
                    n = v

            if n == None:
                return None

            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []

                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]

                reconst_path.append(start)
                reconst_path.reverse()
                return reconst_path

            # for all the neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n

                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)

            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)
        return None
