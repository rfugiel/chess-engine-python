from src.board import Board

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


