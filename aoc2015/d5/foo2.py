from aocframework import AoCFramework

class Day(AoCFramework):
    test_cases = ()
    def go(self):
        raw = self.puzzle_input.rstrip()
        raw_split = self.linesplitted
        def is_nice(word):
            # double chars
            d_iter = [''.join(i) for i in zip(word,word[1:])]
            has_doubles = any(len(word.split(pair))>2 for pair in d_iter)

            # repeat letter
            double_iter = zip(word,word[2:])
            has_double = any(a==b for a,b in double_iter)
            return has_double and has_doubles
        nice_counter = 0
        for word in raw_split:
            nice_counter+=(1 if is_nice(word) else 0)
        return nice_counter

Day()
