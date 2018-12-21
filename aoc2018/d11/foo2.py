from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = ()

    def go(self):
        raw = self.raw_puzzle_input.rstrip()
        raw_split = self.linesplitted
        grid_serial_number = int(raw)
        def calculate_power_level(coords):
            x,y = coords
            power_level = 0
            rack_id = x + 10
            power_level+=(rack_id*y+grid_serial_number)*rack_id
            power_level = (power_level//100) % 10 - 5
            return power_level
        def get_part_pl(coords,size):
            x, y = coords
            return sum(power_level_field[(x+x_offset,y+y_offset)] for x_offset in range(size) for y_offset in range(size))
        power_level_field={(x,y):calculate_power_level((x,y)) for x in range(301) for y in range(301)}
        power_level_sums_total = {}
        for s in range(1,301):
            power_level_sums = {}
            for x in range(301-s):
                for y in range(301-s):
                    power_level_sums[(x,y)]=get_part_pl((x,y),s)
            max_item = max(power_level_sums,key=power_level_sums.get)
            max_val = power_level_sums[max_item]
            power_level_sums_total[(*max_item,s)]=max_val
            print(max_item,max_val,s)
        total_max_item = max(power_level_sums_total,key=power_level_sums_total.get)
        total_max_val = power_level_sums_total[total_max_item]
        return total_max_item,total_max_val

Day()