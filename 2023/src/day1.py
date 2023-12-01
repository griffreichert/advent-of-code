import utils


lines = utils.read_list(__file__, as_str=True)


def get_first_and_last_nums(line):
    num_list = [int(ch) for ch in line if ch.isdigit()]
    return int(str(f"{num_list[0]}{num_list[-1]}"))


_p1 = sum(get_first_and_last_nums(line) for line in lines)

print(f"p1\n{utils.Ansii.green}{_p1}{utils.Ansii.clear}")

# shoutout the boy Aidan for some clever string manipulation
nums_dict = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine",
}

_p2 = 0
for line in lines:
    for num, num_map in nums_dict.items():
        line = line.replace(num, num_map)
    _p2 += get_first_and_last_nums(line)


print(f"p2\n{utils.Ansii.green}{_p2}{utils.Ansii.clear}")
