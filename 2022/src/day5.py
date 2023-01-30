import re
import copy

with open('../data/day5.txt', 'r') as f:
    cargo, moves = f.read().split('\n\n')

cargo = [re.sub(r'[^\w]', ' ', c).replace('    ', '-').replace(' ', '').replace('-', ' ') for c in cargo.split('\n')[:-1]]

moves = moves.split('\n')

print(cargo)

# initialize empty lists representing the cargo for each crane
cranes = [[] for i in range(len(cargo[0]))]

# reverse cargo to put bottom crates on first 
for c in reversed(cargo):
    for i in range(len(c)):
        if c[i] != ' ':
            cranes[i].append(c[i])

# use deepcopy to create a second object of the starting order of cargo for part 2
cranes2 = copy.deepcopy(cranes)

for m in moves:
    move_num, orig, dest = tuple(map(int, re.findall(r'\d+', m)))
    
    # get index of lists for origin and destination crane
    orig = orig - 1
    dest = dest - 1
    
    # list for part 2 to move multiple items in one go
    tmp_stack = []
    for i in range(move_num):
        # part 1, move one box at a time
        cranes[dest].append(cranes[orig].pop())
        # part 2, move boxes in a stack
        tmp_stack.insert(0, cranes2[orig].pop())
    for item in tmp_stack:
        cranes2[dest].append(item)

# # add last item from each list into a string
top_str_1 = ''.join([crane[-1] for crane in cranes])
top_str_2 = ''.join([crane[-1] for crane in cranes2])

print(f'\nPart 1\n{top_str_1}')
print(f'\nPart 2\n{top_str_2}')