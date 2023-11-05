import re
import numpy as np

# adjacents is just north south east west (not including current pos)
adjacents = ((1, 0), (0, 1), (-1, 0), (0, -1))
# neighbors includes diagonal corners (still not current pos)
neighbors = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

adjacents_3d = ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1))


class Ansii:
    green = "\u001b[32m"
    clear = "\u001b[0m"


def add_tuples(a, b):
    return tuple(x + y for x, y in zip(a, b))


def char_to_int(char) -> int:
    """find the int representation of a char
    lowercase go from 97-122 so shift it to 1-26
    uppercase go from 65-90 so shift it to 27-52
    """
    item_int = ord(char)
    return item_int - 96 if item_int >= 97 else item_int - 38


def dict_min_max_indecies(dict) -> tuple:
    return min(dict, key=dict.get), max(dict, key=dict.get)


def find_int(s: str, all=False):
    res = re.findall("\d+", s)
    if all:
        return [int(i) for i in res]
    return int(res[0])


def lines_to_grid(lines, as_numpy=True):
    # if there are spaces between numbers then split them by that
    if " " in lines[0].strip():
        grid = [[int(x) for x in line.strip().split(" ") if x != ""] for line in lines]
    # otherwise numbers will just be treated as individual digits
    else:
        grid = [[int(i) for i in list(line)] for line in lines]
    # convert list to numpy
    if as_numpy:
        grid = np.array(grid)
    return grid


def list_product(_list: list) -> int:
    """find the product of the elements in a list"""
    res = 1
    for x in _list:
        res *= x
    return res


def list_to_int(_list: list) -> int:
    return int("".join(str(x) for x in _list))


def median(points: list) -> int:
    # Sort the list of points
    sorted_points = sorted(points)

    # Calculate the median
    num_points = len(sorted_points)
    if num_points % 2 == 1:
        median = sorted_points[num_points // 2]
    else:
        median = (
            sorted_points[num_points // 2 - 1] + sorted_points[num_points // 2]
        ) // 2
    return median


def read_list(file, as_str=False) -> list:
    with open(f"../data/day{find_int(file.split('/')[-1])}.txt", "r") as f:
        lines = f.read().strip().split("\n")
    if not as_str:
        try:
            #  cast the list to all ints if they are all numerics
            lines = [int(line) for line in lines]
        except:
            pass
    return lines


def tuple_max(list_of_tuples) -> tuple:
    """given a list of tuples, return the element wise maximum

    ex: [(x, y), ... ] -> (max_x, max_y)
    """
    list_of_tuples = list(list_of_tuples)
    return tuple(
        max(tup[dim] for tup in list_of_tuples) for dim in range(len(list_of_tuples[0]))
    )


def show_grid(grid, map={0: ".", 1: "#"}):
    print()
    n, m = grid.shape
    for i in range(n):
        for j in range(m):
            print(map[grid[i, j]], end=" ")
        print()
    print()


# if all(all(char.isnumeric() for char in line) for line in lines):
# import requests
# response = requests.get("https://adventofcode.com/2021/day/1/input")
# print(response.text)

"""
import pyperclip

# Get the clipboard content
clipboard_text = pyperclip.paste()

# Specify the file path where you want to save the text
file_path = 'clipboard_text.txt'

# Write the clipboard content to the file
with open(file_path, 'w') as file:
    file.write(clipboard_text)

print(f'Clipboard content saved to {file_path}')
"""
