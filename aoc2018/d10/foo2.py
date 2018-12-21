from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = ()

    def go(self):
        raw = self.raw_puzzle_input
        raw_split = self.linesplitted

        class Point():
            x = 0
            y = 0
            vel_x = 0
            vel_y = 0

            def __init__(self, x, y, vel_x, vel_y):
                self.x = x
                self.y = y
                self.vel_x = vel_x
                self.vel_y = vel_y

            def move(self):
                self.x += self.vel_x
                self.y += self.vel_y
                return (self.x, self.y)

            def __repr__(self):
                return f"Point @ ({self.x},{self.y}) >>> ({self.vel_x, self.vel_y})"

        points = []
        for line in raw_split:
            splitted_line = line.split(',')
            pointx = int(splitted_line[0][-6:].strip())
            pointy = int(splitted_line[1][1:7].strip())
            pointvelx = int(splitted_line[1][-2:].strip())
            pointvely = int(splitted_line[2][1:3].strip())

            points.append(Point(pointx, pointy, pointvelx, pointvely))
        point_positions = {}

        def distance(x1, y1, x2, y2):
            return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        for i in range(20000):
            next_positions = [point.move() for point in points]
            point_positions[i] = {'pos': next_positions}
            max_x = max(point.x for point in points)
            max_y = max(point.y for point in points)
            min_x = min(point.x for point in points)
            min_y = min(point.y for point in points)
            point_positions[i]['max_distance'] = distance(min_x, min_y, max_x, max_y)
            if point_positions[i]['max_distance'] < 70:
                print(i)
                for y in range(min_y, max_y + 1):
                    for x in range(min_x, max_x + 1):
                        point_at_pos = any(point.x == x and point.y == y for point in points)
                        print('*' if point_at_pos else '.', end='')
                    print('')
                print('')

            # print(min_x,min_y,max_x,max_y,distance(min_x,min_y,max_x,max_y))
        distances = [point_position['max_distance'] for point_position in point_positions.values()]
        min_distance = min(distances)
        print(min_distance)

Day()