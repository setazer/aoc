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
        def get_part_pl(coords):
            x, y = coords
            total_pl=0
            for x_offset in range(3):
                for y_offset in range(3):
                    total_pl+=power_level_field[(x+x_offset,y+y_offset)]
            return total_pl
        power_level_field={(x,y):calculate_power_level((x,y)) for x in range(301) for y in range(301)}
        power_level_sums={}
        for x in range(299):
            for y in range(299):
                power_level_sums[(x,y)]=get_part_pl((x,y))
        max_item = max(power_level_sums,key=power_level_sums.get)
        max_val = power_level_sums[max_item]
        with open('field.txt','w') as field, open('sums.txt','w') as sums:
            for x in range(301):
                for y in range(301):
                    field.write(f"{power_level_field[(x,y)]} ")
                field.write("\n")
            for x in range(299):
                for y in range(299):
                    sums.write(f"{power_level_sums[(x,y)]} ")
                sums.write("\n")
        return max_item,max_val

Day()