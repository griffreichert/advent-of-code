import utils

snailfish = utils.read_list(__file__, as_str=True)


def snailfish_magnitude(snailfish: str):
    """Just multiply by 3 when crossing '['
    divide by 2 when crossing ']'
    and change multiplier by multiplier / 3 * 2 when crossing ','
    This will result in the multiplier to be the correct number when hitting a number, which we can then just multiply and add it to the total.
    """
    total = 0
    multiplier = 1
    for char in snailfish:
        if char.isdigit():
            total += multiplier * int(char)
        elif char == ",":
            multiplier = multiplier // 3 * 2
        elif char == "[":
            multiplier *= 3
        elif char == "]":
            multiplier //= 2
    return total


def reduce_snailfish(snailfish):
    depth = 0
    i = 0
    while True:
        # get all the way through without exploding
        while i < len(snailfish):
            # are we dealing with a digit or a symbol
            char = snailfish[i]
            # dont need to do anything for a comma
            if char == ",":
                pass
            # increase depth
            elif char == "[":
                depth += 1
            # decrease depth
            elif char == "]":
                depth -= 1
            # dealing with a digit
            else:
                double_digit = snailfish[i + 1].isdigit()
                # explode if depth greater than 4
                if depth > 4:
                    # pairs left value (if any) is added to the first number to the left
                    # find the first value to the left
                    l = i - 2
                    while not snailfish[l].isdigit():
                        l -= 1  # keep moving left
                        if i < 0:
                            break
                            # todo
                    first_left_num = snailfish[l]
                    # bump in case it's a double digit
                    first_left_bump = 0
                    # check if left is a double digit number
                    if snailfish[l - 1].isdigit():
                        l -= 1
                        first_left_num += int(snailfish[l]) * 10
                        first_left_bump = 1

                    # add left value from the pair to the first number on the left
                    if double_digit:
                        lnum = int(snailfish[i : i + 2])
                    else:
                        lnum = int(snailfish[i])

                    first_left_num += lnum
                    
                    # rebuild snailfish
                    snailfish = f'{snailfish[:l]}{lnum}{snailfish[l+first_left_bump+1:i-2]}

                    # pairs right value is added to the first number to the right
                    # the pair is replaced with the regular number 0
                else:
                    # dont check this number twice
                    if double_digit:
                        i += 1
            # next number
            i += 1

            # print("\n", i)
            # pprint(snailfish)
            num, depth = snailfish[i]

            # explode the leftmost pair with depth greater than 4
            if depth > 4:
                # print()
                # print("exploding", i, (num, snailfish[i + 1][0]), "with depth", depth)
                prev_chunk = []
                chunk = []
                next_chunk = []
                nnum, _ = snailfish[i + 1]
                # pairs left value (if any) is added to the first number to the left
                if i > 0:
                    prev_num, prev_depth = snailfish[i - 1]
                    prev_chunk = snailfish[: i - 1]
                    chunk.append((prev_num + num, prev_depth))

                # the pair is replaced with the regular number 0
                chunk.append((0, depth - 1))

                # pairs right value is added to the first number to the right
                if i < len(snailfish) - 2:
                    nxt_num, nxt_depth = snailfish[i + 2]
                    next_chunk = snailfish[i + 3 :]
                    chunk.append((nxt_num + nnum, nxt_depth))

                snailfish = prev_chunk + chunk + next_chunk
                # show_snailfish(snailfish)
                # if you did explode, check the position one back
                if i > 0:
                    i -= 1
                continue
            i += 1

        # once you make it to the end of exploding, try splitting
        i = 0
        while i < len(snailfish):
            num, depth = snailfish[i]
            # Split the leftmost number greater than or equal to 10
            if num >= 10:
                # calculate the L and R parts of a num, even numbers split into two,
                # odd numbers are split 13 -> (6, 7)
                left = num // 2
                right = (num + 1) // 2

                snailfish = (
                    snailfish[:i]
                    + [(left, depth + 1), (right, depth + 1)]
                    + snailfish[i + 1 :]
                )
                # print()
                # print("splitting", i, num)
                # show_snailfish(snailfish)
                # if you split, start exploding again from that position
                break
            i += 1

        # if you got through splitting without finding something to split, youre done
        else:
            return snailfish


def combine_snailfish(a, b):
    return [(a_num, a_depth + 1) for a_num, a_depth in a] + [
        (b_num, b_depth + 1) for b_num, b_depth in b
    ]


snailfish = [parse_snail_num(s) for s in snailfish]

# p1 - add all snailfish numbers and find the largest magnitude
final_snailfish = snailfish[0]
for s in snailfish[1:]:
    final_snailfish = reduce_snailfish(combine_snailfish(final_snailfish, s))

_p1 = snailfish_magnitude(final_snailfish)
print("p1")
# p2 - find largest magnitude from adding any of two different snailfish numbers in list
# bruteus forceus - iterate over all combos (except the same)
magnitudes = []
for i, si in enumerate(snailfish):
    for j, sj in enumerate(snailfish):
        if i == j:
            continue
        else:
            mag = snailfish_magnitude(reduce_snailfish(combine_snailfish(si, sj)))
            magnitudes.append((mag, i, j))

print(max(magnitudes, key=lambda x: x[0]))


def p2():
    res = 0
    return res


_p2 = p2()

print(f"p1\n{utils.Ansii.green}{_p1}{utils.Ansii.clear}")
print(f"p2\n{utils.Ansii.green}{_p2}{utils.Ansii.clear}")


# def parse_snail_num(s):
#     snail_num = []
#     depth = 0
#     for c in s:
#         if c == ",":
#             continue
#         elif c == "[":
#             depth += 1
#         elif c == "]":
#             depth -= 1
#         else:
#             snail_num.append((int(c), depth))

#     return snail_num


# def show_snailfish(snailfish):
#     print("[", end=" ")
#     for num, depth in snailfish:
#         color = ""
#         if depth > 4:
#             color = utils.Ansii.red
#         elif num >= 10:
#             color = utils.Ansii.yellow
#         print(f"{color}{num}{utils.Ansii.clear}", end=", ")
#     print()


# def snailfish_magnitude(snailfish):
#     # recursively take 3 * left + 2 * right
#     while len(snailfish) > 1:
#         i = 0
#         while i < len(snailfish) - 1:
#             cur_num, cur_depth = snailfish[i]
#             nxt_num, nxt_depth = snailfish[i + 1]
#             if cur_depth == nxt_depth:
#                 snailfish = (
#                     snailfish[:i]
#                     + [(3 * cur_num + 2 * nxt_num, cur_depth - 1)]
#                     + snailfish[i + 2 :]
#                 )
#                 i -= 1
#             i += 1
#     return snailfish[0][0]
#     """Just multiple by 3 when crossing '[', divide by 2 when crossing ']' and change multiplier by multiplier / 3 * 2 when crossing ','. This will result in the multiplier to be the correct number when hitting a number, which we can then just multiply and add it to the total."""


# def reduce_snailfish(snailfish):
#     i = 0
#     while True:
#         # try to go through without exploding
#         while i < len(snailfish):
#             # print("\n", i)
#             # pprint(snailfish)
#             num, depth = snailfish[i]

#             # explode the leftmost pair with depth greater than 4
#             if depth > 4:
#                 # print()
#                 # print("exploding", i, (num, snailfish[i + 1][0]), "with depth", depth)
#                 prev_chunk = []
#                 chunk = []
#                 next_chunk = []
#                 nnum, _ = snailfish[i + 1]
#                 # pairs left value (if any) is added to the first number to the left
#                 if i > 0:
#                     prev_num, prev_depth = snailfish[i - 1]
#                     prev_chunk = snailfish[: i - 1]
#                     chunk.append((prev_num + num, prev_depth))

#                 # the pair is replaced with the regular number 0
#                 chunk.append((0, depth - 1))

#                 # pairs right value is added to the first number to the right
#                 if i < len(snailfish) - 2:
#                     nxt_num, nxt_depth = snailfish[i + 2]
#                     next_chunk = snailfish[i + 3 :]
#                     chunk.append((nxt_num + nnum, nxt_depth))

#                 snailfish = prev_chunk + chunk + next_chunk
#                 # show_snailfish(snailfish)
#                 # if you did explode, check the position one back
#                 if i > 0:
#                     i -= 1
#                 continue
#             i += 1

#         # once you make it to the end of exploding, try splitting
#         i = 0
#         while i < len(snailfish):
#             num, depth = snailfish[i]
#             # Split the leftmost number greater than or equal to 10
#             if num >= 10:
#                 # calculate the L and R parts of a num, even numbers split into two,
#                 # odd numbers are split 13 -> (6, 7)
#                 left = num // 2
#                 right = (num + 1) // 2

#                 snailfish = (
#                     snailfish[:i]
#                     + [(left, depth + 1), (right, depth + 1)]
#                     + snailfish[i + 1 :]
#                 )
#                 # print()
#                 # print("splitting", i, num)
#                 # show_snailfish(snailfish)
#                 # if you split, start exploding again from that position
#                 break
#             i += 1

#         # if you got through splitting without finding something to split, youre done
#         else:
#             return snailfish


# def combine_snailfish(a, b):
#     return [(a_num, a_depth + 1) for a_num, a_depth in a] + [
#         (b_num, b_depth + 1) for b_num, b_depth in b
#     ]


# snailfish = [parse_snail_num(s) for s in snailfish]

# # p1 - add all snailfish numbers and find the largest magnitude
# final_snailfish = snailfish[0]
# for s in snailfish[1:]:
#     final_snailfish = reduce_snailfish(combine_snailfish(final_snailfish, s))

# _p1 = snailfish_magnitude(final_snailfish)
# print("p1")
# # p2 - find largest magnitude from adding any of two different snailfish numbers in list
# # bruteus forceus - iterate over all combos (except the same)
# magnitudes = []
# for i, si in enumerate(snailfish):
#     for j, sj in enumerate(snailfish):
#         if i == j:
#             continue
#         else:
#             mag = snailfish_magnitude(reduce_snailfish(combine_snailfish(si, sj)))
#             magnitudes.append((mag, i, j))

# print(max(magnitudes, key=lambda x: x[0]))


# def p2():
#     res = 0
#     return res


# _p2 = p2()

# print(f"p1\n{utils.Ansii.green}{_p1}{utils.Ansii.clear}")
# print(f"p2\n{utils.Ansii.green}{_p2}{utils.Ansii.clear}")
