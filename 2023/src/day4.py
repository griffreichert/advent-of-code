import utils


lines = utils.read_lines(__file__, parse_ints=False)


cards = {
    utils.find_ints(line.split(":")[0])[0]: tuple(
        utils.find_ints(part) for part in line.split(":")[-1].split("|")
    )
    for line in lines
}
# TODO refactor this using regex search
# re.search("(...) = \((...), (...)\)", line).groups()


def p1():
    num_winners = [sum(n in winners for n in nums) for nums, winners in cards.values()]
    return sum(2 ** (nw - 1) for nw in num_winners if nw > 0)


def p2():
    card_counts = {i + 1: 1 for i in range(len(cards))}
    for i, (nums, winners) in cards.items():
        for j in range(i + 1, min(len(cards), i + sum(n in winners for n in nums)) + 1):
            card_counts[j] += card_counts[i]
    return sum(card_counts.values())


print(f"p1\n{utils.Ansii.green}{p1()}{utils.Ansii.clear}")
print(f"p2\n{utils.Ansii.green}{p2()}{utils.Ansii.clear}")
