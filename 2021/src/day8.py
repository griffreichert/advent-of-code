import utils

lines = utils.read_lines(__file__, parse_ints=True)


def p1(lines: list):
    res = 0
    for line in lines:
        _, output = line.split("|")
        output = output.strip().split(" ")
        res += sum(1 for signal in output if len(signal) in [2, 3, 4, 7])
    return res


def p2(lines):
    """

      0:      1:      2:      3:      4:
     aaaa    ....    aaaa    aaaa    ....
    b    c  .    c  .    c  .    c  b    c
    b    c  .    c  .    c  .    c  b    c
     ....    ....    dddd    dddd    dddd
    e    f  .    f  e    .  .    f  .    f
    e    f  .    f  e    .  .    f  .    f
     gggg    ....    gggg    gggg    ....

    5:      6:      7:      8:      9:
     aaaa    aaaa    aaaa    aaaa    aaaa
    b    .  b    .  .    c  b    c  b    c
    b    .  b    .  .    c  b    c  b    c
     dddd    dddd    ....    dddd    dddd
    .    f  e    f  .    f  e    f  .    f
    .    f  e    f  .    f  e    f  .    f
     gggg    gggg    ....    gggg    gggg

    """

    true_patterns = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9,
    }

    res = 0

    for line in lines:
        signals, output = line.split("|")
        signals = list(
            sorted([set(sig) for sig in signals.strip().split(" ")], key=len)
        )

        wires = {" ": " "}

        # parse the unique signals
        sig_1 = [sig for sig in signals if len(sig) == 2][0]
        sig_7 = [sig for sig in signals if len(sig) == 3][0]
        sig_4 = [sig for sig in signals if len(sig) == 4][0]

        # a: 7 subtract 1
        a = list(sig_7.difference(sig_1))[0]
        wires[a] = "a"

        # g: len_6 [0, 6, 9], find 9 subtract 4, 7
        for sig in signals:
            if len(sig) == 6 and sig_4.union(sig_7).issubset(sig):
                g = list(sig.difference(sig_4.union(sig_7)))[0]
                wires[g] = "g"
                break
        else:
            print(" !!! no g", g)
            return -1

        sig_9 = sig_4.union({a, g})

        # d: len_5 [2, 3, 5], find the 3, subtract 7, g
        for sig in signals:
            if len(sig) == 5 and sig_7.union({g}).issubset(sig):
                d = list(sig.difference(sig_7.union({g})))[0]
                wires[d] = "d"
                break
        else:
            print(" !!! no d", d)
            return -1

        sig_3 = sig_7.union({d, g})

        # b: 4 subtract 3
        b = list(sig_4.difference(sig_3))[0]
        wires[b] = "b"

        # e: len_6 [0, 6, 9] but not 9 subtract sig_9
        for sig in signals:
            if len(sig) == 6 and not sig_9.issubset(sig):
                e = list(sig.difference(sig_9))[0]
                wires[e] = "e"
                break
        else:
            print(" !!! no e", e)
            return -1

        # c: len_5 [2, 3, 5], find the 2, subtract a, e, d, g
        for sig in signals:
            if len(sig) == 5 and {a, d, e, g}.issubset(sig):
                c = list(sig.difference({a, d, e, g}))[0]
                wires[c] = "c"
                break
        else:
            print(" !!! no c", c)
            return -1

        # f: 1 subtract c
        f = list(sig_1.difference({c}))[0]
        wires[f] = "f"

        # translate the mappings of the wires in the output
        output = "".join(wires[s] for s in output.strip())
        # turn the translated chunks in the output into their signal mappings based on the pattern
        values = [
            true_patterns["".join(s for s in sorted(o))] for o in output.split(" ")
        ]
        # combine digits into one number
        res += utils.list_to_int(values)

    return res


print("p1")
print(p1(lines))
print("p2")
print(p2(lines))
