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


print("Let's play Battleships Arcade")
print("X marks a hit")
print("- marks a miss")
print_board(board)


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


ship_row = random_row(board)
ship_column = random_column(board)


"""
For loop that only allows 5 turns
"""
TURN = 0

for turn in range(5):
    """
    Allows the user to pick a row and a column and whether they hit a ship
    """
    choose_row = int(input('Choose Row (0-5): '))
    choose_column = int(input('Choose Column (0-5): '))

    if choose_row == ship_row and choose_column == ship_column:
        print('Well done, Battleship was sunk!')
        board[choose_row][choose_column] = "X"
        print_board(board)
        break
    else:
        """
        Tells user whether their pick was in range,
        or if they have picked those num/cols before
        """
        if choose_row not in range(6) or choose_column not in range(6):
            print('This is outside the board range, please try again')
        elif board[choose_row][choose_column] == "-":
            print("You have guessed that already")
        else:
            print('You missed, try again!')
            board[choose_row][choose_column] = "-"
            turn = turn + 1
        """
        Tells you whether you have run out of turns
        """
        if turn == 5:
            print("Game over! You Lose.")
        print_board(board)
    print("Turn: ", turn + 1)
