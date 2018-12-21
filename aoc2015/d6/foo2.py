from aocframework import AoCFramework

class Day(AoCFramework):
    test_cases = ()
    def go(self):
        raw = self.puzzle_input.rstrip()
        raw_split = self.linesplitted
        ligths = {(x,y):0 for x in range(1000) for y in range(1000)}
        import re
        for command in raw_split:
            m = re.match(r'(.*)\ (.*) through (.*)', command)
            action, coords1, coords2 = m.groups()
            x1, y1 = map(int, coords1.split(','))
            x2, y2 = map(int, coords2.split(','))
            for x in range(x1,x2+1):
                for y in range(y1,y2+1):
                    if action == 'turn on':
                        ligths[(x,y)]+=1
                    elif action == 'turn off':
                        ligths[(x,y)]-=(1 if ligths[(x,y)]>0 else 0)
                    elif action == 'toggle':
                        ligths[(x, y)] += 2
        return sum(ligths.values())

Day()
