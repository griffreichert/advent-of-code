import copy

import utils

lines = utils.read_lines(__file__, parse_ints=True)


def check_line(line):
    c1 = c2 = False
    # all increasing or all decreasing
    if list(sorted(line)) == list(line) or list(sorted(line, reverse=True)) == list(
        line
    ):
        c1 = True
    for i in range(len(line) - 1):
        step = abs(line[i + 1] - line[i])
        if step > 3 or step < 1:
            break
    else:
        c2 = True
    if c1 and c2:
        return 1
    return 0


def p1():
    res = 0

    for line in lines:
        res += check_line(line)
    return res


def p2():
    res = 0
    for line in lines:
        full_res = check_line(line)
        if full_res:
            res += full_res
        else:
            for i in range(len(line)):
                line_copy: list = copy.deepcopy(line)
                line_copy.pop(i)
                r = check_line(line_copy)
                if r:
                    res += r
                    break
    return res


print(f"p1\n{utils.Ansii.green}{p1()}{utils.Ansii.clear}")
print(f"p2\n{utils.Ansii.green}{p2()}{utils.Ansii.clear}")
