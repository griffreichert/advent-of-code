import utils
from collections import defaultdict


lines = utils.read_lines(__file__, parse_ints=False)


def p1():
    # only 12 red cubes, 13 green cubes, and 14 blue cubes possible
    res = 0
    for i, line in enumerate(lines):
        line = line[line.find(":") + 1 :].strip()
        for game in line.split(";"):
            colors = [
                tuple(colstr.strip().split(" ")) for colstr in game.strip().split(",")
            ]
            colors = {b: int(a) for a, b in colors}
            if not all(
                colors.get(color, 0) <= color_max
                for color, color_max in [("red", 12), ("green", 13), ("blue", 14)]
            ):
                break
        else:
            # add index of possible lines
            res += i + 1
    return res


def p2():
    res = 0
    for line in lines:
        line = line[line.find(":") + 1 :].strip()
        colors_needed = defaultdict(int)
        for game in line.split(";"):
            colors = [tuple(colstr.strip().split(" ")) for colstr in game.split(",")]
            colors = {b: int(a) for a, b in colors}
            for col, draws in colors.items():
                colors_needed[col] = max(colors_needed[col], draws)
        res += utils.list_product(colors_needed.values())
    return res


_p1 = p1()
_p2 = p2()

print(f"p1\n{utils.Ansii.green}{_p1}{utils.Ansii.clear}")
print(f"p2\n{utils.Ansii.green}{_p2}{utils.Ansii.clear}")
