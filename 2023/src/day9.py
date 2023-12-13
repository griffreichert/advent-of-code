import utils


lines = utils.read_list(__file__, as_str=False)
lines = [[int(i) for i in line.split(" ")] for line in lines]


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


_p1 = p1()
_p2 = p2()


print(f"p1\n{utils.Ansii.green}{_p1}{utils.Ansii.clear}")
print(f"p2\n{utils.Ansii.green}{_p2}{utils.Ansii.clear}")
