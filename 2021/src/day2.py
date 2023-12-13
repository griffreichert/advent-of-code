import utils

lines = utils.read_lines(__file__)


def p1(lines):
    pos, depth = 0, 0
    dir_map = {
        "up": -1,
        "down": 1,
    }
    for line in lines:
        direction, unit = line.split(" ")
        unit = int(unit)
        if direction == "forward":
            pos += unit

        else:
            depth += unit * dir_map[direction]

    return pos * depth


def p2(lines):
    pos, depth, aim = 0, 0, 0
    dir_map = {
        "up": -1,
        "down": 1,
    }
    for line in lines:
        direction, unit = line.split(" ")
        unit = int(unit)
        if direction == "forward":
            pos += unit
            depth += aim * unit
        else:
            aim += unit * dir_map[direction]
    return pos * depth


print("p1")
print(p1(lines))
print("p2")
print(p2(lines))
