from aocframework import AoCFramework


def is_visible(trees, i, j, rows_n, cols_n):
    return (
            all(trees[(i,j)] > trees[(i, tn)] for tn in range(j))
            or all(trees[(i,j)] > trees[(tw, j)] for tw in range(i))
            or all(trees[(i,j)] > trees[(i, ts)] for ts in range(j+1, cols_n))
            or all(trees[(i,j)] > trees[(te, j)] for te in range(i+1, rows_n))
    )

def scenicness(trees, i, j, rows_n, cols_n):
    result = 1
    cur_tree = trees[(i,j)]

    dist = 1
    for dist, tn in enumerate(range(j-1,-1,-1), 1):
        cmp_tree = trees[(i, tn)]
        if cmp_tree >= cur_tree:
            break
    result *= dist

    dist = 1
    for dist, tw in enumerate(range(i-1,-1,-1), 1):
        cmp_tree = trees[(tw, j)]
        if cmp_tree >= cur_tree:
            break
    result *= dist

    dist = 1
    for dist, ts in enumerate(range(j+1, cols_n), 1):
        cmp_tree = trees[(i, ts)]
        if cmp_tree >= cur_tree:
            break
    result *= dist

    dist = 1
    for dist, te in enumerate(range(i+1, rows_n), 1):
        cmp_tree = trees[(te, j)]
        if cmp_tree >= cur_tree:
            break
    result *= dist
    return result

class DayPart1(AoCFramework):
    test_cases = (
        ('''30373
25512
65332
33549
35390''', 21),
    )
    known_result = 1870

    def go(self):
        trees = {}
        rows_n = len(self.linesplitted)
        cols_n = len(self.linesplitted[0])
        for y, row in enumerate(self.linesplitted):
            for x, col in enumerate(row.strip()):
                trees[(x,y)] = int(col)

        visible = 0
        for i in range(rows_n):
            for j in range(cols_n):
                if i in (0, rows_n) or j in (0, rows_n):
                    visible +=1
                    continue
                visible += is_visible(trees, i, j, rows_n, cols_n)

        return visible


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''30373
25512
65332
33549
35390
''', 8),
    )
    known_result = None

    def go(self):
        trees = {}
        rows_n = len(self.linesplitted)
        cols_n = len(self.linesplitted[0])
        for y, row in enumerate(self.linesplitted):
            for x, col in enumerate(row.strip()):
                trees[(x,y)] = int(col)

        return max(scenicness(trees, i, j,rows_n, cols_n) for i in range(1,rows_n-1) for j in range(1,cols_n-1))



DayPart2()
