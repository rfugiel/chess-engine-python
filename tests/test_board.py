from src.board import Board

def test_out_of_bounds_check():
    b = Board()
    assert b.is_oob(0) == False
    assert b.is_oob(30) == False
    assert b.is_oob(63) == False
    assert b.is_oob(64) == True
    assert b.is_oob(-1) == True