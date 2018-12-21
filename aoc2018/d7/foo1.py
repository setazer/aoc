from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = ()

    def go(self):
        raw = self.raw_puzzle_input
        raw_split = self.linesplitted
        prerequisites = {}
        all_steps = set()
        for cond in raw_split:
            _,step_parent,*_,step_child,_,_ = cond.split()
            prerequisites.setdefault(step_child,[])
            prerequisites[step_child].append(step_parent)
            all_steps.add(step_parent)
            all_steps.add(step_child)
        available_picks = []
        path =''
        # pick roots
        roots = [key for key in all_steps if not prerequisites.get(key)]

        available_picks +=roots
        while available_picks:
            next_pick = available_picks.pop(available_picks.index(min(available_picks)))
            path+=next_pick
            candidates = [candidate for candidate,requirements in prerequisites.items() if all(req in path for req in requirements)]
            for candidate in candidates:
                candidate_prerequisites = prerequisites.get(next_pick,[''])
                if all(step in path for step in candidate_prerequisites) and not (candidate in path or candidate in available_picks):
                    available_picks.append(candidate)
        return path

Day()