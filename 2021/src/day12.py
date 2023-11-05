import utils
from collections import deque, defaultdict


lines = utils.read_list(__file__, as_str=True)

caves = defaultdict(list)
big_caves = set()
small_caves = set()

for line in lines:
    c1, c2 = line.split("-")
    # dont link back to start
    if c2 != "start":
        caves[c1].append(c2)
    if c1 != "start":
        caves[c2].append(c1)
    # big caves are capitals
    if c1 == c1.upper():
        big_caves.add(c1)
    else:
        small_caves.add(c1)
    if c2 == c2.upper():
        big_caves.add(c2)
    else:
        small_caves.add(c2)


def p1():
    paths = 0
    # initialise queue with current pos, and path
    queue = deque((("start", ("start",)),))
    while queue:
        pos, path = queue.popleft()
        # if we've reached the end stop
        if pos == "end":
            paths += 1
            continue
        # iterate over adjacent caves
        for adj in caves[pos]:
            # can always visit a big cave, or a new small cave
            if adj in big_caves or adj not in path:
                queue.append((adj, path + (adj,)))
    return paths


def p2():
    paths = 0
    # initialise queue with current pos, path, and the small cave we've visited twice
    queue = deque((("start", ("start",), None),))
    while queue:
        pos, path, small_twice = queue.popleft()
        # if we've reached the end stop
        if pos == "end":
            paths += 1
            continue
        # iterate over adjacent caves
        for adj in caves[pos]:
            # can always visit a big cave, or a new small cave
            if adj in big_caves or adj not in path:
                queue.append((adj, path + (adj,), small_twice))
            # if i havent yet visited a small cave twice:
            elif small_twice == None:
                queue.append((adj, path + (adj,), adj))
    return paths


_p1 = p1()
_p2 = p2()

print(
    f"p1\n{utils.Ansii.green}{_p1}\n{utils.Ansii.clear}p2{utils.Ansii.green}\n{_p2}{utils.Ansii.clear}"
)
