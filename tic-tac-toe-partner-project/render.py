# Renders the board from a list of moves
# Version 4
# - added clear_board(board) -> empties an existing board
# - added return_clear_board() -> returns a new blank board
# - added has_winner(board) -> returns True if there's a winner
# - added get_win_symbol(board) -> returns what the winning symbol is
# - added trigger_on_winner(board, func) -> triggers the function upon finding a winner
from art import *
from copy import deepcopy
from typing import Callable


# awesome dynamic solution from https://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards
def merge_strings(prev_str: str, next_str: str) -> str:
    """Utility function that merges two multiline strings together, prev_str and next_str."""
    return "\n".join(["  ".join(elem) for elem in zip(prev_str.split("\n"), next_str.split("\n"))])


def clear_board(board: list) -> None:
    """Clears a board passed as an argument by reassigning each entry to EMPTY"""
    for row in board:
        for x in range(3):
            row[x] = EMPTY


def return_clear_board() -> list:
    """Returns a fresh board instance"""
    board = []
    for x in range(3):
        row = []
        for y in range(3):
            row.append(EMPTY)
        board.append(row)
    return board


def has_winner(board: list) -> bool:
    """Returns True if the board contains a winner or False if one isn't found."""
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return True
    return False


def get_win_symbol(board: list) -> str | None:
    """Returns the winning symbol if there's a winner, else None."""
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    return None


def trigger_on_winner(board: list, func: Callable) -> None:
    """Will execute a passed function is triggered upon finding a winner.

    Intended to replace some repeated code between functions."""
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            func()
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            func()
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        func()
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        func()


def parse_win_symbol(symbol: str) -> str:
    if symbol == X:
        return X_WIN
    elif symbol == O:
        return O_WIN
    else:
        return "ERROR: blank board somehow registered a winner"  # testing odd behavior


def parse_win(board: list) -> list:
    """Sets winning symbols and returns a new board if there's a winner, otherwise returns the old board."""
    if has_winner(board):
        new_board = deepcopy(board)  # make deep copy to avoid mutating original board

        for row in new_board:
            if row[0] == row[1] == row[2] and row[0] != EMPTY:
                win_symbol = parse_win_symbol(row[0])
                for x in range(3):
                    row[x] = win_symbol
                break
        for col in range(3):
            if new_board[0][col] == new_board[1][col] == new_board[2][col] and new_board[0][col] != EMPTY:
                win_symbol = parse_win_symbol(new_board[0][col])
                for x in range(3):
                    new_board[x][col] = win_symbol
                break
        if new_board[0][0] == new_board[1][1] == new_board[2][2] and new_board[0][0] != EMPTY:
            win_symbol = parse_win_symbol(new_board[0][0])
            for x in range(3):
                new_board[x][x] = win_symbol
        if new_board[0][2] == new_board[1][1] == new_board[2][0] and new_board[0][2] != EMPTY:
            win_symbol = parse_win_symbol(new_board[0][2])
            for x in range(3):
                new_board[2 - x][x] = win_symbol
        return new_board
    return board  # else just return the board


def draw_board(board: list) -> None:
    """Takes a list of the current moves on the board and prints them. Changes the color of the winning combo."""
    row_strings = []
    x = 1

    for row in parse_win(board):
        row_str = left_bound.format(num=x)
        for elem in row:
            row_str = merge_strings(row_str, elem)
            row_str = merge_strings(row_str, col_sep)
        row_strings.append(row_str)
        x += 1

    print(abc, end="")
    print(board_art.format(
        row1=row_strings[0],
        row2=row_strings[1],
        row3=row_strings[2],
    ))


# FOR QUICK TESTING
#
# table = [
#     [X, X, O],
#     [EMPTY, X, EMPTY],
#     [EMPTY, EMPTY, X],
# ]
# table = return_clear_board()
# draw_board(table)
