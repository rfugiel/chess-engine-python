from piece import Piece

def check_oob(func):
    # TODO: if this is a wrapper how do I ensure which argument idx is? keyword?
    pass

class Board:
    def __init__(self, board):
        self.board = board if board else [None for _ in range(64)]

    def get_piece_color(self, idx):
        # TODO: Should I make custom exceptions for OOB and Empty?
        if self.is_oob(idx):
            raise Exception("Out of bounds")
        if self.is_empty(idx):
            return Exception("Empty square")
        return Piece(self.board[idx]).color

    def get_piece_type(self, idx):
        # TODO: should I make check oob a wrapper function since I use it a couple places?
        if self.is_oob(idx):
            raise Exception("Out of Bounds")
        if self.is_empty(idx):
            return Exception("Empty square")
        return Piece(self.board[idx]).type

    @staticmethod
    def is_oob(idx):
        # TODO: naming convention - should it be is_oob? oob? should I have not_oob methods for readability?
        return 0 <= idx < 64

    def is_occupied(self, idx):
        if self.is_oob(idx):
            raise Exception("Out of bounds")
        return self.board[idx] is not None

    def is_opponent_piece(self, idx, opponent_idx):
        if self.is_oob(idx):
            raise Exception("Out of bounds")
        return Piece(self.board[idx]).color == Piece(self.board[opponent_idx]).color
