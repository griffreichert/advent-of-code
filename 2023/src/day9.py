import utils


lines = utils.read_lines(__file__, parse_ints=True)


def line_differences(line):
    return [b - a for a, b in zip(line, line[1:])]


def p1():
    res = 0
    for line in lines:
        history = []
        history.append(line)
        while not all(k == 0 for k in history[-1]):
            history.append(line_differences(history[-1]))
        # add the new 0
        history[-1].append(0)
        for i in reversed(range(len(history) - 1)):
            history[i].append(history[i][-1] + history[i + 1][-1])
        res += history[0][-1]
    return res


def p2():
    res = 0
    for line in lines:
        history = []
        history.append(list(reversed(line)))  # just reverse the input line for pt 2!!
        while not all(k == 0 for k in history[-1]):
            history.append(line_differences(history[-1]))
        # add the new 0
        history[-1].append(0)
        for i in reversed(range(len(history) - 1)):
            history[i].append(history[i][-1] + history[i + 1][-1])
        res += history[0][-1]
    return res


print(f"p1\n{utils.Ansii.green}{p1()}{utils.Ansii.clear}")
print(f"p2\n{utils.Ansii.green}{p2()}{utils.Ansii.clear}")
