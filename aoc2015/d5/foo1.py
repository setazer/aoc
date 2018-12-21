from aocframework import AoCFramework
from string import ascii_lowercase as letters
vowels = 'aoeui'

class Day(AoCFramework):
    test_cases = ()
    def go(self):
        def is_nice(word:str):
            # naughty
            naugthy = any(comb in word for comb in ['ab','cd','pq','xy'])
            if naugthy:
                return False
            # 3 vowels
            vowels_count = 0
            for vowel in vowels:
                vowels_count+=word.count(vowel)
            # double letters
            double_letters = any(letter*2 in word for letter in letters)
            return vowels_count>2 and double_letters

        raw = self.puzzle_input.rstrip()
        raw_split = self.linesplitted
        nice_words = 0
        for line in raw_split:
            if is_nice(line):
                nice_words+=1
        return nice_words


Day()
