from collections import defaultdict
from heapq import heappop, heappush

with open('../data/day24.txt') as f:
    lines = f.read().strip().split('\n')

# Test case: pt1 expects 18, pt2 expects 54
# lines = """#E######
# #>>.<^<#
# #.<..<<#
# #>v.><>#
# #<^v^^>#
# ######.#""".split('\n')

blizzards = defaultdict(list)
rocks = {}

n, m = len(lines), len(lines[0])
start, end = (0, 0), (0, 0)

print((n, m))

for i in range(n):
    for j in range(m):
        cur = lines[i][j]
        if cur == '#':
            rocks[(i, j)] = 1
        elif cur not in 'E.':
            blizzards[(i, j)].append(cur)
        else:
            if i == 0:
                start = (i, j)
            elif i == n-1:
                end = (i, j)
    
arrow_dir = {
    '^': (-1, 0),
    '>': (0, 1),
    '<': (0, -1),
    'v': (1, 0)
}
    
def move_blizzards(bliz):
    new_bliz = defaultdict(list)
    for pos, blist in bliz.items():
        for arrow in blist:
            # element wise add the position with the tuple corresponding to the move ddirection
            new_pos = tuple(x + y for x, y in zip(pos, arrow_dir[arrow]))
            # print(pos, arrow, new_pos)
            if new_pos[0] == 0:
                new_pos = (n - 2, new_pos[1])
            elif new_pos[0] == n-1:
                new_pos = (1, new_pos[1])
            elif new_pos[1] == 0:
                new_pos = (new_pos[0], m - 2)
            elif new_pos[1] == m-1:
                new_pos = (new_pos[0], 1)
            new_bliz[new_pos].append(arrow)
    return new_bliz
            
def show(bliz, pos=start):
    for i in range(n):
        for j in range(m):
            tup = (i, j)
            if pos == tup:
                print('E', end=' ')
            elif tup in rocks:
                print('#', end=' ')
            elif tup in bliz:
                if len(bliz[tup]) > 1:
                    print(len(bliz[tup]), end = ' ')
                else:
                    print(bliz[tup][0], end = ' ')
            else:
                print(' ', end=' ')
        print()
    print()

# list[i] represents the positions of all blizzards at minute i
blizzards_list = [blizzards]
for _ in range(1, 1000):
    blizzards_list.append(move_blizzards(blizzards_list[-1]))

def migrate(start_pos, end_pos, start_minute=0):
    # you can stay at the same position so (0,0) must be in the adj list too
    adj = ((1, 0), (0, 1), (0, -1), (0, 0), (-1, 0))
    # heap stores the minute and position
    heap = [(start_minute, start_pos)]
    # set to hold duplicate locations to prune the heap
    dups = set()
    while True:
        minute, pos = heappop(heap)
        # return once you have reached the end
        if pos == end_pos:
            return minute - start_minute
    
        next_bliz = blizzards_list[minute + 1]
        # iterate over adjacent positions
        for new_pos in [tuple(x + y for x, y in zip(pos, a)) for a in adj]:
            # if in the next minute, an adjacent space is open, add that to the queue
            if (new_pos not in rocks) and (new_pos not in next_bliz) and ((0,0) <= new_pos < (n, m)):
                # if you reached a position in the same number of minutes, skip adding duplicates to the heap
                if (new_pos, minute+1) not in dups:
                    dups.add((new_pos, minute+1))
                    heappush(heap, (minute+1, new_pos))

# show(blizzards)
trip_a = migrate(start, end)
print('Part 1:', trip_a)
trip_b = migrate(start_pos=end, end_pos=start, start_minute=trip_a)
trip_c = migrate(start, end, start_minute=trip_a+trip_b)
print('Part 2:', sum((trip_a, trip_b, trip_c)))
