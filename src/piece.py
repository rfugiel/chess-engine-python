class Piece(object):
    # TODO: Should these enums be in piece?
    WHITE = 0
    BLACK = 1

    PAWN = "p"
    ROOK = "r"
    BISHOP = "b"
    KNIGHT = "n"
    QUEEN = "q"
    KING = "k"

    def __init__(self, encoding):
        self.color = encoding[0]
        self.type = encoding[1]

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, val):
        if val == "0":
            self._color = Piece.WHITE
        if val == "1":
            self._color = Piece.BLACK

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, val):
        self._type = {
            "p": Piece.PAWN,
            "r": Piece.ROOK,
            "b": Piece.BISHOP,
            "n": Piece.KNIGHT,
            "q": Piece.QUEEN,
            "k": Piece.KING,
        }.get(val)
