from aocframework import AoCFramework
from hashlib import md5

class Day(AoCFramework):
    test_cases = ()
    def go(self):
        raw = self.puzzle_input.rstrip()
        raw_split = self.linesplitted
        n=0
        with open("md5.txt","w") as f:
            while True:
                n+=1
                md5hash = md5(f"{raw}{n}".encode('utf-8')).hexdigest()
                if md5hash.startswith("000000"):
                    return n

Day()
