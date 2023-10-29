import re
import numpy as np

adjacents = ((1, 0), (0, 1), (-1, 0), (0, -1))
neighbors = ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1))


def find_int(s: str, all=False):
    res = re.findall("\d+", s)
    if all:
        return [int(i) for i in res]
    return int(res[0])


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
    # if all(all(char.isnumeric() for char in line) for line in lines):


def char_to_int(char) -> int:
    """find the int representation of a char
    lowercase go from 97-122 so shift it to 1-26
    uppercase go from 65-90 so shift it to 27-52
    """
    item_int = ord(char)
    return item_int - 96 if item_int >= 97 else item_int - 38


def lines_to_grid(lines, as_numpy=True):
    grid = [[int(x) for x in line.strip().split(' ') if x != ''] for line in lines]
    if as_numpy:
        grid = np.array(grid)
    return grid

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
