from .piece import Piece


class Knight(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)

    def is_valid_move(self, board, start_y, start_x, end_y, end_x):
        if abs(start_y - end_y) == 1 and abs(start_x - end_x) == 2 or abs(start_y - end_y) == 2 and abs(start_x - end_x) == 1:
            return True
        return False

    def __str__(self):
        color = 'White' if self.is_white else 'Black'
        return f'{color}, Knight'
