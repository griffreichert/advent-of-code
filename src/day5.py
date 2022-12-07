import re
from pprint import pprint
import copy

# list to hold lines of cargo, to be reversed later
lines = []
with open('../data/day5_cranes.txt', 'r') as f:
    for line in f:
        line = re.sub(r'[^\w]', ' ', line).replace('    ', '-').replace(' ', '').replace('-', ' ')
        lines.append(line)

# initialize empty lists representing the cargo for each crane
cranes = [[] for i in range(len(lines[0]))]

# reverse cargo to put bottom crates on first 
for line in reversed(lines):
    for i in range(len(line)):
        if line[i] != ' ':
            cranes[i].append(line[i])
        
# pprint(cranes)
# use deepcopy to create a second object of the starting order of cargo for part 2
cranes2 = copy.deepcopy(cranes)

with open('../data/day5_moves.txt', 'r') as f:
    for line in f:
        move_num, orig, dest = line.replace('move ', '').replace('from ', '').replace('to ', '').split(' ')
        # get index of lists for origin and destination crane
        orig = int(orig) - 1
        dest = int(dest) - 1
        # print(f'\nmove: {move_num}  orig: {orig}  dest: {dest}')
        
        # list for part 2 to move multiple items in one go
        tmp_stack = []
        for i in range(int(move_num)):
            # part 1, move one box at a time
            cranes[dest].append(cranes[orig].pop())
            # part 2, move boxes in a stack
            tmp_stack.insert(0, cranes2[orig].pop())
        for item in tmp_stack:
            cranes2[dest].append(item)

# pprint(cranes)
# pprint(cranes2)

# add last item from each list into a string
top_str_1 = ''.join([crane[-1] for crane in cranes])
top_str_2 = ''.join([crane[-1] for crane in cranes2])

print(f'\nPart 1\n{top_str_1}')
print(f'\nPart 2\n{top_str_2}')


# print(f'\nPart 2\nnumber of pairs where one range overlaps the other: {spaces.overlap.sum()}')
