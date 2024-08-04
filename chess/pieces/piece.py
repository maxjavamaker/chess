class Piece:
    def __init__(self, is_white):
        self.is_white = is_white

    def is_valid_move(self, board, start_y, start_x, end_y, end_x):
        """
        Attempt to move the piece to the specified (row, col).
        Returns True if move is valid, False otherwise.
        """
        pass  # Implement movement logic specific to each piece

    def get_all_moves(self, board, start_y, start_x):
        pass

    def __str__(self):
        """ Return string representation of the piece (e.g., 'White Pawn', 'Black Knight') """
        pass
