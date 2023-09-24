from collections import defaultdict


class Supply:

    def __init__(self, demo=False):
        self.moves = []
        self.stacks = defaultdict(list)
        self.open_file(demo)

    def open_file(self, demo):
        with open(f'day-5{demo and "-demo" or ""}.txt', 'r') as file:
            for line in file:
                if '[' in line:
                    for idx, char in enumerate(line):
                        if not (idx - 1) % 4 and char != ' ':
                            self.stacks[int((idx - 1) / 4 + 1)].insert(0, char)
                elif line.startswith('move'):
                    self.moves.append([int(x) for x in line.split() if x.isdigit()])

    def solve(self, part):
        for count, idx_from, idx_to in self.moves:
            if part == 1:
                for _ in range(count):
                    self.stacks[idx_to].append(self.stacks[idx_from].pop())
            elif part == 2:
                self.stacks[idx_to] += self.stacks[idx_from][-count:]
                self.stacks[idx_from] = self.stacks[idx_from][:-count]
        sorted_stacks = dict(sorted(self.stacks.items())).values()
        print(''.join([stack[-1] for stack in sorted_stacks]))


supply_demo = Supply(demo=True)
supply_demo.solve(1)  # CMZ

supply_demo = Supply(demo=True)
supply_demo.solve(2)  # MCD

supply = Supply(demo=False)
supply.solve(1)  # VJSFHWGFT

supply = Supply(demo=False)
supply.solve(2)  # LCTQFBVZV
