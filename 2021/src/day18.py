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
            if i <= 0 or i >= len(snailfish) - 1:
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

    while True:
        depth = 0
        i = 0
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
                    new_snailfish = ""
                    # get the current number (left in the pair)
                    cur_left = get_int_from_indices(i, j)

                    # find the first value to the left
                    left_indices = traverse_until_digit(i - 1, forwards=False)
                    # pairs left value is added to the first number to the left (if any)
                    if left_indices:
                        left_start, left_end = left_indices
                        new_left = get_int_from_indices(left_start, left_end)
                        new_left += cur_left
                        # reconstruct the snailfish so far
                        # assume it has brackets to each side
                        new_snailfish += f"{snailfish[:left_start]}{new_left}{snailfish[left_end+1:i-1]}"
                    else:
                        new_snailfish += f"{snailfish[:i-1]}"

                    # replace the current number with 0
                    new_snailfish += "0"

                    # find right number in the current pair
                    ri = j + 2
                    while not snailfish[ri].isdigit():
                        ri += 1
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
                    # set the snailfish to the new snailfish
                    snailfish = new_snailfish
                    # move i back to the beginning and reset depth
                    depth = 0
                    i = -1
            i += 1

        # once you make it to the end of exploding, try splitting
        i = 0
        while i < len(snailfish) - 1:
            if snailfish[i].isdigit() and snailfish[i + 1].isdigit():
                cur = get_int_from_indices(i, i + 1)
                l = cur // 2
                r = (cur + 1) // 2
                snailfish = f"{snailfish[:i]}[{l},{r}]{snailfish[i+2:]}"
                break
            i += 1

        # if you got through splitting without finding something to split, youre done
        else:
            return snailfish


# p1 - add all snailfish numbers and find the largest magnitude
final_snailfish = snailfish[0]
for s in snailfish[1:]:
    final_snailfish = reduce_snailfish(f"[{final_snailfish},{s}]")

_p1 = snailfish_magnitude(final_snailfish)
print(f"p1\n{utils.Ansii.green}{_p1}{utils.Ansii.clear}")

# p2 - find largest magnitude from adding any of two different snailfish numbers in list
# bruteus forceus - iterate over all combos (except the same)
magnitudes = []
for i, si in enumerate(snailfish):
    for j, sj in enumerate(snailfish):
        if i == j:
            continue
        else:
            mag = snailfish_magnitude(reduce_snailfish(f"[{si},{sj}]"))
            magnitudes.append((mag, i, j))

_p2, mi, mj = max(magnitudes, key=lambda x: x[0])

print(f"p2\n{utils.Ansii.green}{_p2}{utils.Ansii.clear}")
