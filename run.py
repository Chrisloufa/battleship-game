# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from random import randint


board = []
"""
Creates battleship playing board
"""
for i in range(0, 6):
    board.append(['O'] * 6)


def print_board(board):
    """
    Makes the board cleaner and easier to look at
    """
    for row in board:
        print(' ' .join(row))


def random_row(board):
    """
    Adds a random int to the row
    """
    return randint(0, len(board) - 1)


def random_column(board):
    """
    Adds a random int to the column
    """
    return randint(0, len(board) - 1)


random_row(board)
random_column(board)
print_board(board)
