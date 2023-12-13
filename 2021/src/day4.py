import utils
import itertools
import numpy as np
from pprint import pprint

lines = utils.read_lines(__file__)

# parse bingo numbers
bingo_numbers = utils.find_ints(lines[0])

# parse and store boards
boards = [list(group) for line, group in itertools.groupby(lines[2:], key=bool) if line]
boards = list(map(utils.lines_to_grid, boards))


def evaluate_bingo(board):
    # Check rows for Bingo
    rows_bingo = np.any(np.all(board == 1, axis=1))

    # Check columns for Bingo
    columns_bingo = np.any(np.all(board == 1, axis=0))

    # # Check diagonals for Bingo
    # diagonal_bingo = np.all(np.diag(board) == 1) or np.all(np.diag(np.fliplr(board)) == 1)

    # Check if any of the checks resulted in a Bingo
    return rows_bingo or columns_bingo  # or diagonal_bingo


def p1():
    # reset scoreboards
    scoreboards = [np.zeros((5, 5), dtype="int") for _ in boards]

    for draw in bingo_numbers:
        # call off a bingo numbers
        for board, scoreboard in zip(boards, scoreboards):
            scoreboard[np.where(board == draw)] = 1

            # check for bingo
            if evaluate_bingo(scoreboard):
                unmarked = np.sum(board[np.where(scoreboard == 0)])
                return draw * unmarked

    return -1


def p2():
    # reset scoreboards
    scoreboards = [np.zeros((5, 5), dtype="int") for _ in boards]
    possible = list(range(len(boards)))
    for draw in bingo_numbers:
        # call off a bingo numbers
        for board_index, (board, scoreboard) in enumerate(zip(boards, scoreboards)):
            scoreboard[np.where(board == draw)] = 1

            # check for bingo
            if evaluate_bingo(scoreboard):
                # if last board:
                if len(possible) == 1 and board_index == possible[0]:
                    unmarked = np.sum(board[np.where(scoreboard == 0)])
                    print(draw, unmarked)
                    return draw * unmarked

                if board_index in possible:
                    possible.remove(board_index)

    return -1


print("p1")
print(p1())
print("p2")
print(p2())
