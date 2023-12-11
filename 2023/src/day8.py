import utils
import itertools
import math


lines = utils.read_list(__file__, as_str=True)
turns = list(lines[0])
graph = {
    line.split(" = ")[0]: tuple(
        node.strip()
        for node in line.replace("(", "").replace(")", "").split(" = ")[1].split(", ")
    )
    for line in lines[2:]
}


def solve_maze(start, ends):
    cur = start
    directions = itertools.cycle(turns)
    steps = 0
    while cur not in ends:
        steps += 1
        turn = next(directions)
        if turn == "L":
            i = 0
        else:
            i = 1
        cur = graph[cur][i]

    return steps


def p1():
    return solve_maze("AAA", {"ZZZ"})


def p2():
    locs = [node for node in graph if node[-1] == "A"]
    ends = set(node for node in graph if node[-1] == "Z")
    steps = [solve_maze(loc, ends) for loc in locs]
    return math.lcm(*steps)


_p1 = p1()
_p2 = p2()

print(f"p1\n{utils.Ansii.green}{_p1}{utils.Ansii.clear}")
print(f"p2\n{utils.Ansii.green}{_p2}{utils.Ansii.clear}")
