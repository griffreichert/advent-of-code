import re
from pathlib import Path

import numpy as np

# adjacents is just north south east west (not including current pos)
adjacents = ((1, 0), (0, 1), (-1, 0), (0, -1))
# neighbors includes diagonal corners (still not current pos)
neighbors = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

diagonals = ((-1, -1), (-1, 1), (1, -1), (1, 1))

adjacents_3d = ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1))


class Ansii:
    red = "\u001b[31m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    blue = "\u001b[34m"
    purple = "\u001b[35m"
    cyan = "\u001b[36m"

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


def find_ints(s: str):
    return [int(i) for i in re.findall(r"-?\d+", s)]


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


def list_product(list: list) -> int:
    """find the product of the elements in a list"""
    res = 1
    for x in list:
        res *= x
    return res


def list_to_int(list: list) -> int:
    return int("".join(str(x) for x in list))


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


def read_lines(file, parse_ints=False) -> list:
    data_path = Path(__file__).parents[1] / "data"
    with open(data_path / f"day{find_ints(file.split('/')[-1])[0]}.txt", "r") as f:
        lines = f.read().strip().split("\n")
    if parse_ints:
        try:
            #  cast the list to all ints if they are all numerics
            lines = [find_ints(line) for line in lines]
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


def bubble_sort(list_to_sort, comparison_function):
    """given a list and a comparison function, bubble sort a list

    Args:
        list_to_sort (list): list to sort, can be tuples or whatever
        comparison_function (function): function that will sort the list, should take two arguments and return true if the first is less than the second

    Returns:
        _type_: _description_
    """
    for i in range(len(list_to_sort)):
        for j in reversed(range(1, i + 1)):
            if not comparison_function(list_to_sort[j - 1], list_to_sort[j]):
                tmp = list_to_sort[j - 1]
                list_to_sort[j - 1] = list_to_sort[j]
                list_to_sort[j] = tmp
    return list_to_sort


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
