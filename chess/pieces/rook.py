from .piece import Piece


class Rook(Piece):
    def __init__(self, is_white):
        super().__init__(is_white)
        self.has_moved = False

    def is_valid_move(self, board, start_y, start_x, end_y, end_x):
        if start_x == end_x:
            return self.check_blocking_pieces_vertical(board, start_y, end_y, start_x)
        elif start_y == end_y:
            return self.check_blocking_pieces_horizontal(board, start_y, end_y, start_x)
        return False

    def check_blocking_pieces_vertical(self, board, start_y, end_y, x):
        direction = 1 if start_y < end_y else -1
        for y in range(start_y + direction, end_y):
            if board[y][x] is not None:
                return False
        self.has_moved = True
        return True

    def check_blocking_pieces_horizontal(self, board, y, start_x, end_x):
        direction = 1 if start_x < end_x else -1
        for x in range(start_x + direction, end_x):
            if board[y][x] is not None:
                return False
        self.has_moved = True
        return True

    def __str__(self):
        color = 'White' if self.is_white else 'Black'
        return f'{color}, Rook'
