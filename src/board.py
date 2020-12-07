class Color:
    WHITE = 0
    BLACK = 1


# Maybe we can return move list exceptions object or something (make move_list an object/struct)
# if move_list has exception, return (there are en passant and castling)

# Should these be class methods or methods that take in board? composition vs abstraction...


class Board:
    def __init__(self, board):
        self.board = board if board else [None for _ in range(64)]

    def get_piece_color(self, idx):
        # Raise exception if no piece there?
        pass

    def get_piece_type(self, idx):
        # Raise exception if no piece there
        pass

    def in_bound(self, idx):
        return 0 <= idx < 64

    def is_occupied(self, idx):
        return self.board[idx] is not None

    def is_empty(self, idx):
        return not self.board[idx]

    def is_opponent_piece(self, idx, my_color):
        return True
