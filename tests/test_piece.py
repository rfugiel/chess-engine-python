from src.piece import Piece
# TODO: fix this import, should it be from src?

def test_read_color_from_encoding():
    assert Piece("0p").color == Piece.WHITE
    assert Piece("1p").color == Piece.BLACK


def test_read_type_from_encoding():
    assert Piece("0p").type == Piece.PAWN
    assert Piece("0r").type == Piece.ROOK
    assert Piece("0b").type == Piece.BISHOP
    assert Piece("0n").type == Piece.KNIGHT
    assert Piece("0q").type == Piece.QUEEN
    assert Piece("0k").type == Piece.KING
