import utils

lines = utils.read_lines(__file__, parse_ints=True)


def check_line(line):
    # all increasing or all decreasing
    all_inc_dec: bool = (
        list(sorted(line)) == line or list(sorted(line, reverse=True)) == line
    )
    for i, j in zip(line, line[1:]):
        step = abs(i - j)
        if step > 3 or step < 1:
            break
    else:
        if all_inc_dec:
            return 1
    return 0


def p1():
    return sum(check_line(line) for line in lines)


def p2():
    res = 0
    for line in lines:
        if check_line(line):
            res += 1
        else:
            for i in range(len(line)):
                if check_line(line[:i] + line[i + 1 :]):
                    res += 1
                    break
    return res


print(f"p1\n{utils.Ansii.green}{p1()}{utils.Ansii.clear}")
print(f"p2\n{utils.Ansii.green}{p2()}{utils.Ansii.clear}")
