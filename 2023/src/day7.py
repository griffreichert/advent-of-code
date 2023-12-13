import utils
from collections import Counter


lines = utils.read_lines(__file__, parse_ints=False)


def parse_hand(h):
    face_cards = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
    }
    return [int(face_cards.get(c, c)) for c in h]


def parse_hand_pt2(h):
    face_cards = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 1,  # now the weakest
        "T": 10,
    }
    return [int(face_cards.get(c, c)) for c in h]


def score_hand(hand):
    counts = Counter(hand).most_common()
    # print(hand, counts, counts[0][0])
    if counts[0][1] == 5:
        return 1
    elif counts[0][1] == 4:
        return 2
    elif counts[0][1] == 3:
        # full house
        if counts[1][1] == 2:
            return 3
        else:
            return 4
    elif counts[0][1] == 2:
        # two pair
        if counts[1][1] == 2:
            return 5
        else:
            return 6
    return 7


def tiebreak(a, b):
    # True b is a stronger hand than a
    for ca, cb in zip(a, b):
        if ca == cb:
            continue
        return ca < cb
    assert False, print("tiebreak not decided!!")


def compare_hands(a, b):
    # return true if a is a weaker hand, otherwise we will swap
    a_hand, a_score, _ = a
    b_hand, b_score, _ = b
    if a_score == b_score:
        return tiebreak(a_hand, b_hand)
    return a_score > b_score


def total_winnings(hands):
    return sum(i * bid for i, (_, _, bid) in enumerate(hands, start=1))


def p1():
    hands = []
    for line in lines:
        hand, bid = line.split(" ")
        hand = parse_hand(hand)
        # hand, rank, bid, tiebreak
        hands.append((hand, score_hand(hand), int(bid)))

    hands = utils.bubble_sort(hands, compare_hands)

    return total_winnings(hands)


def p2():
    hands = []
    for line in lines:
        hand, bid = line.split(" ")
        original = parse_hand_pt2(hand)
        bid = int(bid)
        # if i have a joker, replace the highest most common non-joker card
        hand_count = Counter([card for card in original if card != 1])
        if len(hand_count) == 0:
            # if i have all jokers, dont replace them
            optimal = 1
        else:
            optimal = max(
                card
                for card in hand_count
                if hand_count[card] == max(hand_count.values())
            )
        hand = [optimal if card == 1 else card for card in original]
        # hand, rank, bid, tiebreak
        # use original for tiebreaks
        hands.append((original, score_hand(hand), int(bid)))

    ranked_hands = utils.bubble_sort(hands, compare_hands)

    return total_winnings(ranked_hands)


print(f"p1\n{utils.Ansii.green}{p1()}{utils.Ansii.clear}")
print(f"p2\n{utils.Ansii.green}{p2()}{utils.Ansii.clear}")
