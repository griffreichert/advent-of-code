import copy
import numpy as np 

class Monkey:
    def __init__(self, attrs: dict):
        self.items = attrs['items']
        self.operation = attrs['operation']
        self.mod = attrs['mod']
        self.tr = attrs['tr']
        self.fa = attrs['fa']
        self.inspections = 0

    def catch(self, new_item):
        self.items.append(new_item)
        
    def agent_of_chaos_pt1(self):
        while len(self.items) > 0:
            self.inspections += 1
            old = self.items.pop(0)
            # evaluate operartion and floor divide by 3
            new = eval(self.operation) // 3
            # throw item to next monkey
            if new % self.mod == 0:
                monkeys[self.tr].catch(new)
            else:
                monkeys[self.fa].catch(new)

    def agent_of_chaos_pt2(self):
        while len(self.items) > 0:
            self.inspections += 1
            old = self.items.pop(0)
            # evaluate operartion
            # https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html
            # only keep the part that is needed to do the modulo between all the monkeys based on the magic number
            new = eval(self.operation) % magic_number
            # throw item to next monkey
            if new % self.mod == 0:
                monkeys[self.tr].catch(new)
            else:
                monkeys[self.fa].catch(new)
    
with open('../data/day11.txt', 'r') as f:
    text = f.read().split('\n\n')
    
monkey_text = [line.split('\n') for line in text]

monkeys = []
magic_number = 1

for m in monkey_text:
    monkeys.append(Monkey({
        'items': [int(it) for it in m[1][17:].split(',')],
        'operation': m[2][19:],
        'mod': int(m[3][20:]),
        'tr': int(m[4][-1]),
        'fa': int(m[5][-1]),
    }))
    # multiply all the modulo numbers together for part 2 (chinese number theorem)
    magic_number *= int(m[3][20:])
    
# copy for part 2
monkeys_copy = copy.deepcopy(monkeys)

# simulate part 1
for _ in range(20):
    for m in monkeys:
        m.agent_of_chaos_pt1()

# calculate the level of monkey business as the product of the top 2 inspection counts
def monkey_business(monkeys):
    return np.prod(sorted([m.inspections for m in monkeys], reverse=True)[0:2])

print(f'\nPart 1\n{monkey_business(monkeys)}')

# simulate part 2
monkeys = monkeys_copy
for _ in range(10000):
    for m in monkeys:
        m.agent_of_chaos_pt2()

print(f'\nPart 2\n{monkey_business(monkeys)}\n')