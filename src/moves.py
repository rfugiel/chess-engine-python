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
