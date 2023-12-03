from functools import reduce

from aocframework import AoCFramework


class DayPart1(AoCFramework):
    test_cases = (
        ('''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green''', 8),
    )
    known_result = 2512

    def go(self):
        maxes = {
            'red': 12,
            'green': 13,
            'blue': 14,
        }
        raw_split = self.linesplitted
        parsed_games = {}
        for game in raw_split:
            game_id, _, game_data = game.partition(': ')
            game_id = int(game_id.partition(' ')[-1])
            game_list = game_data.split('; ')
            balls_lists = [item.split(', ') for item in game_list]
            parsed_balls_lists = [[(int(item.partition(' ')[0]), item.partition(' ')[-1]) for item in round] for round in balls_lists]
            parsed_games[game_id] = parsed_balls_lists

        result = 0
        for game_id, rounds in parsed_games.items():
            viable = all(maxes[ball_color] >= ball_count for round in rounds for (ball_count, ball_color) in round)
            if not viable:
                continue
            result += game_id

        return result


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green''', 2286),
    )
    known_result = 67335

    def go(self):
        raw_split = self.linesplitted
        parsed_games = {}
        for game in raw_split:
            game_id, _, game_data = game.partition(': ')
            game_id = int(game_id.partition(' ')[-1])
            game_list = game_data.split('; ')
            balls_lists = [item.split(', ') for item in game_list]
            parsed_balls_lists = [[(int(item.partition(' ')[0]), item.partition(' ')[-1]) for item in round] for round in balls_lists]
            parsed_games[game_id] = parsed_balls_lists

        result = 0
        for game_id, rounds in parsed_games.items():
            maxes = {}
            for round in rounds:
                for (ball_count, ball_color) in round:
                    maxes[ball_color] = max(maxes.get(ball_color, 0), ball_count)
            power = reduce(lambda x, y: x*y, maxes.values())
            result += power
        return result

DayPart2()
