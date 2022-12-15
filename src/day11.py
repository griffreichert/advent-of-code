monkeys = []

class Monkey:
    def __init__(self, operation, items=[], test=1, if_true=0, if_false=0):
        self.operation = operation
        self.items = items
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspections = 0

    def add_item(self, new_item):
        self.items.append(new_item)
        
    def agent_of_chaos(self):
        for item in self.items:
            print(item)
        
def make_lambda(op, arg2):
    if arg2 == 'old':
        if op == '*':
            return (lambda x: x * x)
        else:
            return (lambda x: x + x)
    if op == '*':
        if op == '*':
            return (lambda x: x * int(arg2))
        else:
            return (lambda x: x + int(arg2))
        
    
# with open('example..txt'):

lam = make_lambda('*', '5')
print(lam(4))