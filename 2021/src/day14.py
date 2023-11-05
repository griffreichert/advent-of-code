import utils
from collections import Counter


lines = utils.read_list(__file__, as_str=True)


def expand_polymers(iters):
    # polymer string is the first line
    polymer = lines[0]
    # formulas are are the first two chars mapped to the 6th char
    formula = {line[:2]: line[6] for line in lines[2:]}

    # count the number of pairs of two chars
    pairs = Counter(a + b for a, b in zip(polymer, polymer[1:]))
    # count the number of individual chars (important otherwise pairs will double count overlap)
    chars = Counter(polymer)

    for _ in range(iters):
        new_pairs = Counter()
        for (a, b), count in pairs.items():
            # get the char that we will insert based on the formulas
            c = formula[a + b]
            # increase the count of both chunks by the current ammount
            # so this will effectively double each time
            new_pairs[a + c] += count
            new_pairs[c + b] += count
            # the only new char added is the one we increase the count of
            chars[c] += count
        # set the pairs to be the new pairs
        pairs = new_pairs
    # return the difference between most frequent and least frequent
    return max(chars.values()) - min(chars.values())


_p1 = expand_polymers(10)
_p2 = expand_polymers(40)

print(
    f"p1\n{utils.Ansii.green}{_p1}\n{utils.Ansii.clear}p2{utils.Ansii.green}\n{_p2}{utils.Ansii.clear}"
)
