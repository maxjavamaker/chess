from .piece import Piece


class Pawn(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)
        self.has_moved = False  # Track if the pawn has moved

    def is_valid_move(self, board, start_y, start_x, end_y, end_x):
        if abs(start_y - end_y) == 1 and start_x == end_x and board[end_y, end_x] is None:
            if self.is_white and start_y - 1 == end_y:
                self.has_moved = True
                return True
            elif start_y + 1 == end_y:
                self.has_moved = True
                return True
        elif abs(start_y - end_y) == 2 and start_x == end_x and self.has_moved is False:
            if self.is_white and board[start_y - 1, start_x] is None and board[start_y - 2, start_x] is None:
                self.has_moved = True
                return True
            elif board[start_y + 1, start_x] is None and board[start_y + 2, start_x] is None:
                self.has_moved = True
                return True
        elif abs(start_y - end_y) == abs(start_x - end_x) == 1:
            if self.is_white and board[start_y - 1, end_x] is not None:
                self.has_moved = True
                return True
            elif board[start_y + 1, end_x] is not None:
                self.has_moved = True
                return True
        return False

    def __str__(self):
        color = 'White' if self.is_white else 'Black'
        return f'{color}, Pawn'
