from .piece import Piece


class King(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)
        self.has_moved = False  # Track if the king has castled

    def is_valid_move(self, board, start_y, start_x, end_y, end_x):
        if abs(start_y - end_y) <= 1 and abs(start_x - end_x) <= 1:
            self.has_moved = True
            return True
        return False

    def castle(self, board, start_y, start_x, end_y, end_x):
        # Implement castle move for the king
        rook = board[end_y][end_x]
        if not self.has_moved and not rook.has_moved:
            pass  # implement castle logic

    def __str__(self):
        color = 'White' if self.is_white else 'Black'
        return f'{color}, King'
