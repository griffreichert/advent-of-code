import math
import utils

lines = utils.read_lines(__file__, parse_ints=True)
subs = utils.find_ints(lines[0])


def p1(subs):
    # use the median
    return sum(abs(sub - utils.median(subs)) for sub in subs)


def p2(subs):
    avg_float = sum(subs) / len(subs)
    # since we dont know which way to try the average do both and take the min
    return min(
        sum(sum(range(abs(sub - avg) + 1)) for sub in subs)
        for avg in (math.floor(avg_float), math.ceil(avg_float))
    )


print("p1")
print(p1(subs))
print("p2")
print(p2(subs))
