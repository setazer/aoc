from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = ()

    def go(self):
        raw = self.raw_puzzle_input
        raw_split = self.linesplitted
        def hamming2(s1, s2):
            """Calculate the Hamming distance between two bit strings"""
            assert len(s1) == len(s2)
            return sum(c1 != c2 for c1, c2 in zip(s1, s2))
        for box in raw_split:
            matching = [close_box for close_box in raw_split if hamming2(close_box,box)==1]
            if matching:
                return f"{box}\n{matching[0]}"


Day()
hhvsdkatysmiqjxunezgwcdpr
hhvsdkatysmiqjxjunezgwcdpr