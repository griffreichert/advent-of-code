import math
import numpy as np 

monkeys = []

class Monkey:
    def __init__(self, operation, items=[], test=1, if_true=0, if_false=0):
        self.operation = operation
        self.items = items
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspections = 0

    def catch(self, new_item):
        self.items.append(new_item)
        
    def agent_of_chaos(self):
        while len(self.items) > 0:
            item = self.items.pop(0)
            self.inspections += 1
            post_inspect = math.floor(self.operation(item) / 3)
            if post_inspect % self.test == 0:
                monkeys[self.if_true].catch(post_inspect)
            else:
                monkeys[self.if_false].catch(post_inspect)

    def agent_of_chaos_2(self):
        while len(self.items) > 0:
            item = self.items.pop(0)
            self.inspections += 1
            post_inspect = self.operation(item)
            if post_inspect % self.test == 0:
                monkeys[self.if_true].catch(post_inspect)
            else:
                monkeys[self.if_false].catch(post_inspect)
        
def make_lambda(operator, arg2):
    if arg2 == 'old':
        if operator == '*':
            return (lambda x: x * x)
        else:
            return (lambda x: x + x)
    else:
        if operator == '*':
            return (lambda x: x * int(arg2))
        else:
            return (lambda x: x + int(arg2))
        
    
with open('../data/day11.txt', 'r') as f:
    items = []
    operation = None
    test = 1
    if_true = 0
    if_false = 0
    for line in f:
        line = line.replace('\n', '')
        if 'Starting items:' in line:
            items = [int(item) for item in line.replace('  Starting items: ', '').split(',')]
        elif 'Operation:' in line:
            tup = line.replace('  Operation: new = old ', '').split(' ')
            operation = make_lambda(tup[0], tup[1])
        elif '  Test: ' in line:
            test = int(line.split(' by ')[1])
        elif ' If true' in line:
            if_true = int(line[-1])
        elif ' If false' in line:
            if_false = int(line[-1])
            monkeys.append(Monkey(operation, items, test, if_true, if_false))

# print(monkeys)
for i in range(20):
    for m in monkeys:
        m.agent_of_chaos()
    print('\n', i)
    for m in monkeys:
        print(m.items)

monkey_business = sorted([m.inspections for m in monkeys], reverse=True)
print(f'\nPart 1\n{np.prod(monkey_business[0:2])}')

# print(monkeys)
for i in range(10000):
    for m in monkeys:
        m.agent_of_chaos_2()
    if i % 100 == 0:
        print(i)
        print('\n', i)
        for m in monkeys:
            print(m.items)

monkey_business_2 = sorted([m.inspections for m in monkeys], reverse=True)
print(f'\nPart 2\n{np.prod(monkey_business[0:2])}')