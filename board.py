class Color:
    WHITE = 0
    BLACK = 1


def pawn_moves(idx, board):
    move_list = []
    color = board.get_piece_color(idx)

    starting_row_range = range(8, 16) if color == color.WHITE else range(47, 56)
    z = 1 if color == color.WHITE else -1

    # Standard advances
    one_square_up = idx + 8 * z
    if board.in_bounds(one_square_up) and board.is_empty(one_square_up):
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
        if board.in_bounds(m) and board.is_opponent_piece(m, color)
    ]
    move_list += valid_capture_moves

    return move_list


def queen_moves(idx, board):
    move_list = []


# Maybe we can return move list exceptions object or something (make move_list an object/struct)
# if move_list has exception, return (there are en passant and castling)

# Should these be class methods or methods that take in board? composition vs abstraction...


class Board:
    def __init__(self):
        self.board = [None for _ in range(64)]

    def get_piece_color(self, idx):
        # Raise exception if no piece there
        pass

    def get_piece_type(self, idx):
        # Raise exception if no piece there
        pass

    def in_bound(self, idx):
        return 0 <= idx < 64

    def is_occupied(self, idx):
        return self.board[idx]

    def is_empty(self, idx):
        return not self.board[idx]

    def is_opponent_piece(self, idx, my_color):
        return True

    def generate_moves_until_oob_or_hits_piece(self, idx, t):
        """
        Returns move list going in a direction until out of bounds or it hits another piece
        # If hits a piece, includes in move list only if opposite color (capture)
        :param idx: index of piece -> Int
        :param t: Transformation to apply -> Int
        :return: Move list -> List
        """
        move_list = []
        i = idx
        while True:
            i += t
            if not self.in_bound(i):
                break
            elif self.in_bound(i) and self.is_empty(i):
                move_list.append(i)
            elif self.is_occupied(i):
                if self.is_opponent_piece(i):
                    move_list.append(i)
                break

        return move_list


b = Board()

x = b.generate_moves_until_oob_or_hits_piece(0, 8)
print(x)