from aocframework import AoCFramework

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
        total_meta = 0
        def get_node():
            nonlocal total_meta
            children,meta = read_input(2)
            for i in range(int(children)):
                get_node()
            metadata = read_input(int(meta))
            total_meta+=sum(map(int,metadata))
        get_node()
        return total_meta
Day()
