from src.board import Board
from src.piece import Piece

def test_out_of_bounds_check():
    b = Board()
    assert b.is_oob(0) == False
    assert b.is_oob(30) == False
    assert b.is_oob(63) == False
    assert b.is_oob(64) == True
    assert b.is_oob(-1) == True


def test_is_empty_check():
    test_board = [None for _ in range(64)]
    test_board[10] = "0q"

    b = Board(test_board)

    assert b.is_empty(10) == False
    assert b.is_empty(11) == True


def test_piece_color():
    test_board = [None for _ in range(64)]
    test_board[10] = "0q"
    test_board[11] = "1q"

    b = Board(test_board)

    assert b.piece_color(10) == Piece.WHITE
    assert b.piece_color(11) == Piece.BLACK


def test_piece_type():
    test_board = [None for _ in range(64)]
    test_board[10] = "0q"
    test_board[11] = "1n"

    b = Board(test_board)

    assert b.piece_type(10) == Piece.QUEEN
    assert b.piece_type(11) == Piece.KNIGHT

