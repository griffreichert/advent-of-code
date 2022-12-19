from pprint import pprint


with open('../data/day13.txt') as f:
# with open('../data/example.txt') as f:
    lines = f.read().strip().split('\n\n')
    
def compare(l, r):
    # convert mismatches into a comparison of two lists
    if isinstance(l, int) and isinstance(r, list):
        l = [l]
        
    if isinstance(l, list) and isinstance(r, int):
        r = [r]
        
    # if both are integers, the lower integer should come first, if they are equal, keep looking
    if isinstance(l, int) and isinstance(r, int):
        if l > r:
            return 0
        if l < r:
            return 1
        # -1 indicates keep going
        return -1
    
    # if both are lists, compare items in corresponding positions, left list should run out first
    if isinstance(l, list) and isinstance(r, list):
        # check each corresponging item in the list
        for i in range(min(len(l), len(r))):
            c = compare(l[i], r[i])
            # if you get a diffinitive result (1, 0) then return it
            if c != -1:
                return c
        # left list should end first
        if len(l) < len(r):
            return 1
        # right list should not end first
        elif len(l) > len(r):
            return 0
        # if neither list ended, keep comparing 
        return -1

# sum of correct indexes
idx_sum = 0
for i, line in enumerate(lines):
    left, right = map(eval, line.split('\n'))
    c = compare(left, right)
    idx_sum += c * (i + 1)

print(f'\nPart 1\n{idx_sum}')


packets = []
for line in lines:
    left, right = map(eval, line.split('\n'))
    packets.append(left)
    packets.append(right)

key1 = [[2]]
key2 = [[6]]
packets.append(key1)
packets.append(key2)

pprint(packets)

n = len(packets)

# bubble sort
for i in range(n):
    for j in reversed(range(1, i + 1)):
        if compare(packets[j-1], packets[j]) == 0:
            tmp = packets[j-1]
            packets[j-1] = packets[j]
            packets[j] = tmp

pprint(packets)

pt2 = (packets.index(key1) + 1) * (packets.index(key2) + 1)
print(f'\nPart 2\n{pt2}')