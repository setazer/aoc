import pprint
from collections import defaultdict

from aocframework import AoCFramework

def tree():
    return defaultdict(tree)
data_tree = tree()
class Day(AoCFramework):
    test_cases = ()
    def go(self):
        raw = self.puzzle_input.rstrip()
        raw_split = self.linesplitted
        data = raw.split()
        def read_input(num_values):
            nonlocal data
            chunk = data[0:num_values]
            data[0:num_values]=[]
            return tuple(chunk)
        def get_node():
            local_dict={}
            children,meta = read_input(2)
            local_dict['num_children'] = int(children)
            local_dict['children'] = []
            for i in range(int(children)):
                local_dict['children'].append(get_node())
            metadata = read_input(int(meta))
            local_dict['meta']=metadata
            if not int(children):
                local_dict['sum_meta']=sum(map(int,metadata))
            return local_dict
        def get_node_value(tree):
            meta_vals = tree['meta']
            total_value=0
            for value in meta_vals:
                try:
                    total_value+=get_node_value(tree['children'][int(value)-1])
                except IndexError:
                    pass
            print(tree.get('sum_meta',0))
            total_value+=tree.get('sum_meta',0)
            return total_value


        total_tree = get_node()
        return get_node_value(total_tree)
Day()