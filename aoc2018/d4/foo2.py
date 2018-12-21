from aocframework import AoCFramework

class Day(AoCFramework):
    test_cases = ()
    def go(self):
        raw = self.puzzle_input.rstrip()
        raw_split = self.linesplitted
        shifts = sorted(raw_split)

        guards={}
        guard_sleeps={}
        for action in shifts:
            # print(action)
            _,time_,action_desc=action.split(maxsplit=2)
            minute = int(time_[3:5])
            if 'begins shift' in action_desc:
                guard_n=action_desc.split()[1]

            elif 'falls asleep'in action_desc:
                shift_start = minute
            elif 'wakes up' in action_desc:
                shift_end = minute
                for m in range(shift_start,shift_end):
                    guards[(guard_n,m)]=guards.get((guard_n,m),0)+1
                    guard_sleeps[guard_n]=guard_sleeps.get(guard_n,0)+1
        most_sleeps = sorted(guards,key=guards.get,reverse=True)
        longest_sleepers = sorted(guard_sleeps,key=guard_sleeps.get,reverse=True)
        return [(key,guards[key]) for key in most_sleeps if key[0] == longest_sleepers[0]]

Day()
