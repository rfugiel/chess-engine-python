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