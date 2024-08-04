from .piece import Piece
from .queen import Queen


class Bishop(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)

    def is_valid_move(self, board, start_y, start_x, end_y, end_x):
        # Implement bishop-specific movement logic
        if abs(start_y - end_y) == abs(start_x - end_x):
            return Queen.check_blocking_pieces_diagonal(board, start_y, start_x, end_y, end_x)

    def get_all_moves(self, board, start_y, start_x):
        pass
    def __str__(self):
        color = 'White' if self.is_white else 'Black'
        return f'{color}, Bishop'
