from src.piece import Piece

def test_read_color_from_encoding():
    assert  Piece("0p") == Piece.WHITE
    assert  Piece("1p") == Piece.BLACK

def test_read_type_from_encoding():
    assert  Piece("0p") == Piece.PAWN
    assert  Piece("0r") == Piece.ROOK
    assert Piece("0b") == Piece.BISHOP
    assert Piece("0n") == Piece.KNIGHT
    assert Piece("0q") == Piece.QUEEN
    assert Piece("0k") == Piece.KING