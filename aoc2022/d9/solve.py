from aocframework import AoCFramework


class Vector:
    __slots__ = ('x', 'y')

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Vector):
            return (self.x, self.y) == (other.x, other.y)

    def normalize(self):
        return Vector(
            self.x//abs(self.x) if self.x != 0 else 0,
            self.y//abs(self.y) if self.y != 0 else 0,
        )


class Point:
    __slots__ = ('x', 'y', 'walk_distance', 'history')

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.walk_distance = 0
        self.history = {(0, 0)}

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self.x-other.x, self.y-other.y)

    def move(self, vec: Vector):
        self.x += vec.x
        self.y += vec.y
        self.walk_distance += 1
        self.history.add((self.x, self.y))

    def follow(self, head):
        direction: Vector = head - self
        norm_dir = direction.normalize()
        if norm_dir != direction:
            self.move(norm_dir)

    def walked(self):
        return self.walk_distance

    def visited(self):
        return len(self.history)


directions = {
    'U': Vector(0, -1),
    'D': Vector(0, 1),
    'L': Vector(-1, 0),
    'R': Vector(1, 0),
}


class DayPart1(AoCFramework):
    test_cases = (
        ('''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2''', 13),
    )
    known_result = 6464

    def go(self):
        raw_split = self.linesplitted
        head = Point()
        tail = Point()
        for line in raw_split:
            direction, _, times = line.partition(' ')
            for _ in range(int(times)):
                head.move(directions[direction])
                tail.follow(head)

        return tail.visited()


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20''', 36),
    )
    known_result = 2604

    def go(self):
        raw_split = self.linesplitted
        snake = [Point() for _ in range(10)]
        for line in raw_split:
            direction, _, times = line.partition(' ')
            for _ in range(int(times)):
                head = snake[0]
                head.move(directions[direction])
                tails = snake[1:]
                for i, tail in enumerate(tails, 1):
                    tail.follow(snake[i-1])

        return snake[-1].visited()


DayPart2()


class DayCustomPart(AoCFramework):
    test_cases = (('''U 8
R 5
D 3''', 11),)
    known_result = 287

    def go(self):
        raw_split = self.linesplitted
        snake = [Point() for _ in range(2)]
        for line in raw_split:
            direction, _, times = line.partition(' ')
            for _ in range(int(times)):
                head = snake[0]
                head.move(directions[direction])
                tails = snake[1:]
                for i, tail in enumerate(tails, 1):
                    tail.follow(snake[i-1])
                if snake[-1].visited() > 1:
                    snake.append(Point())

        return len(snake)  # minimal length of rope for its tail to never move after all movements

DayCustomPart()
