# A decision-making algorithm for the computer opponent
# Version 2
from copy import deepcopy
from random import choice
from art import EMPTY, X, O


def get_available_moves(board: list) -> list:
    """Looks for all EMPTY slots on the board and returns them as a list of coordinate tuples."""
    tuples = []
    for x in range(3):
        for y in range(3):
            if board[x][y] == EMPTY:
                tuples.append((x, y))
    return tuples


def get_opposite_symbol(symbol: str) -> str:
    if symbol == X:
        return O
    else:
        return X


def look_for_winner(symbol: str, board: list) -> bool:
    """A utility used by the eval_move() function."""
    for row in board:
        if symbol == row[0] == row[1] == row[2]:
            return True
    for col in range(3):
        if symbol == board[0][col] == board[1][col] == board[2][col]:
            return True
    if symbol == board[0][0] == board[1][1] == board[2][2]:
        return True
    if symbol == board[2][0] == board[1][1] == board[0][2]:
        return True
    return False


def eval_move(symbol: str, board: list, depth: int = 0) -> tuple:
    """A function that defines how the computer evaluates potential moves. Returns a tuple representing the row/column
    position of the move it chooses to make.

    The algorithm prioritizes finding a winning move first, then blocking a potential loss. If neither are found,
    it recursively calls itself up to depth rounds, currently hardcoded at 1 round in the future.
    If the algorithm doesn't find an optimal move before hitting depth, it returns (-1, -1).
    """
    # TODO: Somehow eval_move returns NoneType when out of moves and I can't find how
    if depth > 2:
        return -1, -1

    available_moves = get_available_moves(board)
    if len(available_moves) > 1:
        for move in available_moves:
            test_board = deepcopy(board)
            test_board[move[0]][move[1]] = symbol  # move to test

            if look_for_winner(symbol, test_board):  # winning move?
                # print("Winning move found:", move)
                return move if move is not None else (-1, -1)

        for move in available_moves:
            test_board = deepcopy(board)
            test_board[move[0]][move[1]] = get_opposite_symbol(symbol)
            if look_for_winner(get_opposite_symbol(symbol), test_board):  # block a loss?
                # print("Blocking loss:", move)
                return move if move is not None else (-1, -1)

        for move in available_moves:
            test_board = deepcopy(board)
            test_board[move[0]][move[1]] = symbol
            # print("Peering into the future:", move)
            return eval_move(symbol, test_board, depth + 1)  # recursively look into the future up to depth
    return -1, -1


def get_available_corners(board: list) -> list:
    """Returns open corner positions as a list of tuples."""
    corners = []
    if board[0][0] == EMPTY:
        corners.append((0, 0))
    if board[0][2] == EMPTY:
        corners.append((0, 2))
    if board[2][0] == EMPTY:
        corners.append((2, 0))
    if board[2][2] == EMPTY:
        corners.append((2, 2))
    return corners


def set_move(row: int, elem: int, symbol: str, board: list) -> None:
    """Inserts a symbol at the row and element of a given board."""
    board[row][elem] = symbol


def opponent_move(board: list) -> None:
    """A method that carries out which move the computer will make.

    Assumes that the computer will play O's."""
    best_move = eval_move(O, board)  # TODO: No clue where NoneType is coming from
    # print("Best move:", best_move)
    if best_move != (-1, -1) and best_move is not None:
        set_move(best_move[0], best_move[1], O, board)  # if best move, perform move
    else:
        corners = get_available_corners(board)  # otherwise prioritize corners
        if len(corners) > 0:
            corner_move = choice(corners)
            set_move(corner_move[0], corner_move[1], O, board)  # more optimal might be the opposite corner from player
        else:
            move = choice(get_available_moves(board))  # if all else fails, pick a random move
            if move is not None:
                set_move(move[0], move[1], O, board)


