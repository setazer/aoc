from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = ()

    def go(self):
        raw = self.raw_puzzle_input
        raw_split = self.linesplitted
        fabric = {}
        claim_sizes = {}
        for claim in raw_split:

            n,_,coords,size = claim.split(' ')
            x,y = map(int,coords[:-1].split(','))
            width,heigth = map(int,size.split('x'))
            claim_sizes[n]=width*heigth

            for i in range(x+1,x+width+1):
                for j in range(y+1,y+heigth+1):
                    fabric[(i,j)]=(n if not fabric.get((i,j)) else "X")
        patch_list = list(fabric.values())
        for claim,c_size in claim_sizes.items():
            if patch_list.count(claim)==c_size:
                return claim

Day()