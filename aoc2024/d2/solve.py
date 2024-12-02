from itertools import pairwise

from aocframework import AoCFramework


def is_safe(report):
    return (
        (report == sorted(report) or report == sorted(report, reverse=True))
        and not any((abs(x - y) > 3) or (abs(x - y) < 1) for x, y in pairwise(report))
    )


def is_salvagable(report: list):
    for i, _ in enumerate(report):
        salvage = report.copy()
        salvage.pop(i)
        if is_safe(salvage):
            return True
    return False


class DayPart1(AoCFramework):
    test_cases = (
        ('''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9''', 2),
    )
    known_result = None

    def go(self):
        raw_split = self.linesplitted
        reports = [list(map(int, line.split())) for line in raw_split]
        safe_reports = []
        for report in reports:
            if not is_safe(report):
                continue
            safe_reports.append(report)
        return len(safe_reports)


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9''', 4),
    )
    known_result = None

    def go(self):
        raw_split = self.linesplitted
        reports = [list(map(int, line.split())) for line in raw_split]
        safe_reports = []
        for report in reports:
            if not is_safe(report) and not is_salvagable(report):
                continue
            safe_reports.append(report)
        return len(safe_reports)


DayPart2()
