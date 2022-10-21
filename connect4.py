import numpy as np

x = [1, 2, 3, 4, 5, 6, 7]
board = np.zeros((7, 7), dtype=int)
board[0] = x


def display_screen():
    screen = board
    print(screen)


display_screen()

player = int(input("enter your choice: "))


def player_action(player):
    col = player
    num_action = 0
    while num_action != 42:
        num_action += 1
        if not col.isdigit and col <= 7:
            print(update_screen(player, col))
        else:
            return "UNEXPECTED INPUT!"


def update_screen(player, col):
    row = board[7][0]
    while not row == 0:
        if col == 1 and board[row][col] == 0:
            screen = np.where(0, player, board)
            row -= 1
            return update_screen(player, col)
        elif col == 2 and board[row][col] == 0:
            screen = np.where(0, player, board)
            row -= 1
            return update_screen(player, col)
        elif col == 3 and board[row][col] == 0:
            screen = np.where(0, player, board)
            row -= 1
            return update_screen(player, col)
        elif col == 4 and board[row][col] == 0:
            screen = np.where(0, player, board)
            row -= 1
            return update_screen(player, col)
        elif col == 5 and board[row][col] == 0:
            screen = np.where(0, player, board)
            row -= 1
            return update_screen(player, col)
        elif col == 6 and board[row][col] == 0:
            screen = np.where(0, player, board)
            row -= 1
            return update_screen(player, col)
        elif col == 7 and board[row][col] == 0:
            screen = np.where(0, player, board)
            row -= 1
            return update_screen(player, col)


player_action(1)
update_screen(1, col)
