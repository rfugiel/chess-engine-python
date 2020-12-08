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


def starting_board():
    # Returns standard starting board
    test_board = [None for _ in range(64)]

    # Back row - White
    test_board[0] = "0r"
    test_board[1] = "0n"
    test_board[2] = "0b"
    test_board[3] = "0q"
    test_board[4] = "0k"
    test_board[5] = "0b"
    test_board[6] = "0k"
    test_board[7] = "0r"

    # Pawn row - White

    test_board[8] = "0p"
    test_board[9] = "0p"
    test_board[10] = "0p"
    test_board[11] = "0p"
    test_board[12] = "0p"
    test_board[13] = "0p"
    test_board[14] = "0p"
    test_board[15] = "0p"

    # Pawn row - Black

    test_board[48] = "0p"
    test_board[49] = "0p"
    test_board[50] = "0p"
    test_board[51] = "0p"
    test_board[52] = "0p"
    test_board[53] = "0p"
    test_board[54] = "0p"
    test_board[55] = "0p"

    # Back row - Black
    test_board[56] = "1r"
    test_board[57] = "1n"
    test_board[58] = "1b"
    test_board[59] = "1q"
    test_board[60] = "1k"
    test_board[61] = "1b"
    test_board[62] = "1k"
    test_board[63] = "1r"

    return test_board

