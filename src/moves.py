from typing import List

from piece import Piece
from board import Board
from utils import starting_board


def pawn_moves(idx: int, board: Board):
    move_list = []
    color = board.piece_color(idx)

    starting_row_range = range(8, 16) if color == Piece.WHITE else range(47, 56)
    z = 1 if color == Piece.WHITE else -1

    # Standard advances
    one_square_up = idx + 8 * z
    if not board.is_oob(one_square_up) and board.is_empty(one_square_up):
        move_list.append(one_square_up)
        if idx in starting_row_range:  # Two square advance
            two_squares_up = idx + 16 * z
            if board.is_empty(one_square_up):
                move_list.append(two_squares_up)

    # Capture moves
    capture_moves = [idx + 7 * z, idx + 9 * z]
    valid_capture_moves = [
        m
        for m in capture_moves
        if not board.is_oob(m)
        and not board.is_empty(m)
        and board.is_opponent_piece(idx, m)
    ]
    move_list += valid_capture_moves

    return move_list


test_board = starting_board()
test_board[17] = "1q"
b = Board(test_board)
print(pawn_moves(10, b))
