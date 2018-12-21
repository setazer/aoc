from aocframework import AoCFramework
from string import ascii_uppercase as letters

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
        work_times = {letter:letters.index(letter)+61 for letter in letters}
        path =''
        # pick roots
        roots = [key for key in all_steps if not prerequisites.get(key)]

        class Worker:
            work = None
            work_time = 0

            def is_done(self):
                return bool(self.work_time == 0)

            def do_work(self):
                if self.work and self.work_time > 1:
                    self.work_time -= 1
                else:
                    nonlocal path
                    path+=self.work or ''
                    self.work_complete()


            def set_work(self, task):
                self.work = task
                self.work_time = work_times[task]

            def work_complete(self):
                self.work = None
                self.work_time=0
                candidates = [candidate for candidate, requirements in prerequisites.items() if
                              all(req in path for req in requirements)]
                for candidate in candidates:
                    candidate_prerequisites = prerequisites.get(next_pick, [''])
                    if all(step in path for step in candidate_prerequisites) and not (
                            candidate in path or candidate in available_picks or candidate in (worker.work for worker in workers)):
                        available_picks.append(candidate)

            def __repr__(self):
                return f"{self.work}:{self.work_time}"

        workers = [Worker() for _ in range(5)]
        available_picks +=roots
        time = 0
        while True:
            for worker in workers:
                worker.do_work()
            for worker in workers:
                if worker.is_done() and available_picks:
                    print(available_picks, min(available_picks))
                    next_pick = available_picks.pop(available_picks.index(min(available_picks)))
                    worker.set_work(next_pick)
            if not(available_picks or any(worker.work for worker in workers)):
                break
            time += 1



        return time







Day()