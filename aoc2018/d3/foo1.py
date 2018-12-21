from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = ()

    def go(self):
        raw = self.raw_puzzle_input
        raw_split = self.linesplitted
        fabric = {}
        for claim in raw_split:
            n,_,coords,size = claim.split(' ')
            x,y = map(int,coords[:-1].split(','))
            width,heigth = map(int,size.split('x'))

            for i in range(x+1,x+width+1):
                for j in range(y+1,y+heigth+1):
                    fabric[(i,j)]=(n if not fabric.get((i,j)) else "X")
        return list(fabric.values()).count("X")

Day()