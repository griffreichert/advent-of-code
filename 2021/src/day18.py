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
    def traverse_until_digit(index: int, forwards=True) -> int:
        """start at a position and traverse left or right until you find a digit

        Args:
            index (int): starting index
            forwards (bool, optional): whether to traverse forwards or backwards. Defaults to True.

        Returns:
            tuple (int, int): start and end indexes of the number, None if we reach the end in either direction
        """
        i = index
        while not snailfish[i].isdigit():
            if i <= 0 or i >= len(snailfish):
                return None
            if forwards:
                i += 1
            else:
                i -= 1
        start = i
        end = i
        # test for it being a double digit
        # if going forwards, you've just reached the start digit
        if forwards:
            if snailfish[i + 1].isdigit():
                end += 1
        # if going backwards, you've just reached the last digit
        elif not forwards:
            if snailfish[i - 1].isdigit():
                start -= 1

        return start, end

    def get_int_from_indices(i: int, j: int) -> int:
        return int(snailfish[i : j + 1])

    depth = 0
    i = 0
    # while True:
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
            # j stores the end index of the current number
            j = i
            if snailfish[i + 1].isdigit():
                j += 1

            # explode if depth greater than 4
            if depth > 4:
                print("exploding")
                print(i, snailfish[i], depth)
                depth -= 1
                new_snailfish = ""

                # get the current number (left in the pair)
                cur_left = get_int_from_indices(i, j)
                #                                    *
                #                      1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 3 3 3
                #  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2
                #  [ [ [ [ 0 , 7 ] , 4 ] , [ 7 , [ [ 8 , 4 ] , 9 ] ] ] , [ 1 , 1 ] ]

                # find the first value to the left
                left_indices = traverse_until_digit(i - 1, forwards=False)
                print("LL", left_indices)
                # pairs left value is added to the first number to the left (if any)
                if left_indices:
                    left_start, left_end = left_indices
                    new_left = get_int_from_indices(left_start, left_end)
                    new_left += cur_left
                    # reconstruct the snailfish so far
                    # assume it has brackets to each side
                    new_snailfish += (
                        f"{snailfish[:left_start]}{new_left}{snailfish[left_end+1:i-1]}"
                    )
                else:
                    new_snailfish += f"{snailfish[:i-1]}"

                # replace the current number with 0
                new_snailfish += "0"

                # find right number in the current pair
                ri = j + 2
                rj = ri
                if snailfish[ri + 1].isdigit():
                    rj += 1
                cur_right = get_int_from_indices(ri, rj)

                # add right number to the first number to the right if there is any
                right_indices = traverse_until_digit(rj + 1, forwards=True)
                if right_indices:
                    right_start, right_end = right_indices
                    new_right = get_int_from_indices(right_start, right_end)
                    new_right += cur_right
                    new_snailfish += f"{snailfish[rj+2:right_start]}{new_right}{snailfish[right_end+1:]}"
                else:
                    new_snailfish += f"{snailfish[rj+2:]}"
                print(snailfish)
                snailfish = new_snailfish
                print(snailfish)
                # move i
                # i = right_start - 1
            else:
                # get ready to increment i but take into acount the number could be a double digit
                i = j
        # next number
        i += 1

        # # once you make it to the end of exploding, try splitting
        # i = 0
        # while i < len(snailfish):
        #     num, depth = snailfish[i]
        #     # Split the leftmost number greater than or equal to 10
        #     if num >= 10:
        #         # calculate the L and R parts of a num, even numbers split into two,
        #         # odd numbers are split 13 -> (6, 7)
        #         left = num // 2
        #         right = (num + 1) // 2

        #         snailfish = (
        #             snailfish[:i]
        #             + [(left, depth + 1), (right, depth + 1)]
        #             + snailfish[i + 1 :]
        #         )
        #         # print()
        #         # print("splitting", i, num)
        #         # show_snailfish(snailfish)
        #         # if you split, start exploding again from that position
        #         break
        #     i += 1

        # # if you got through splitting without finding something to split, youre done
        # else:
    return snailfish


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
