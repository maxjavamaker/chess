import sys
from typing import Optional, List
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from pieces.pawn import Pawn
from pieces.piece import Piece


class Board:

    def __init__(self):
        self.board: List[List[Optional[Piece]]] = [[None for _ in range(8)] for _ in range(8)]
        self.setup()
        self.white_turn = True  # True means white's turn, False means black's turn

    def move(self, start_y, start_x, end_y, end_x):
        if self.check_for_checkmate():
            self.declare_winner()
        temp = self.board[end_y][end_x]  # stores piece in case move is invalid
        piece = self.board[start_y][start_x]
        if self.is_valid_move(start_y, start_x, end_y, end_x) and piece.is_valid_move(self.board, start_y, start_x, end_y, end_x):
            self.board[end_y][end_x], self.board[start_y][start_x] = piece, None
        if self.check_for_check():  # undo the move
            self.board[start_y][start_x], self.board[end_y][end_x] = piece, temp
        else:
            self.white_turn = not self.white_turn

    def is_valid_move(self, start_y, start_x, end_y, end_x):  # check whose turn to move it is and that the coordinate being moved to is valid
        if self.board[start_y][start_x] is None or self.board[end_y][end_x].is_white != self.white_turn:
            return False
        elif not all(0 <= value < 8 for value in (start_y, start_x, end_y, end_x)):
            return False
        elif self.board[end_y][end_x] is not None and self.board[start_y][start_x].is_white == self.board[end_y][end_x].is_white:
            return False

    def check_for_check(self):  # make sure move did not lead to a check, True if in check
        king_y, king_x, valid = None, None, True
        for i in range(8):
            for j in range(8):
                if str(self.board[i][j]) == ('White' if self.white_turn else 'Black') + 'King':
                    king_x, king_y = i, j
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece is not None and piece.is_white != self.board[king_y][king_x].is_white and piece.is_valid_move(
                        self.board, i, j, king_y, king_x):
                    return True
        return False

    def check_for_checkmate(self):
        if not self.check_for_check():  # Use existing method to check if in check
            return False  # Not in check, hence not checkmate
        king_x, king_y = None, None
        for i in range(8):
            for j in range(8):
                # Find the king of the current player
                if isinstance(self.board[i][j], King) and self.board[i][j].is_white == self.white_turn:
                    king_x, king_y = i, j
                    break

        # Try all possible moves for the current player
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece is not None and piece.is_white == self.white_turn:
                    # Generate all possible moves for this piece
                    for new_y in range(8):
                        for new_x in range(8):
                            if self.is_valid_move(i, j, new_y, new_x) and piece.is_valid_move(self.board, i, j, new_y, new_x):
                                # Make the move temporarily
                                original_piece = self.board[new_y][new_x]
                                self.board[new_y][new_x] = piece
                                self.board[i][j] = None

                                # Validate the move - check if the king is still in check
                                if not self.check_for_check():  # If not in check, this move is valid
                                    # Undo the move
                                    self.board[i][j] = piece
                                    self.board[new_y][new_x] = original_piece
                                    return False  # Found a valid move, hence not checkmate

                                # Undo the move if still in check
                                self.board[i][j] = piece
                                self.board[new_y][new_x] = original_piece

        # If no valid moves are found, it's a checkmate
        return True

    def declare_winner(self):
        print('White' if self.white_turn else 'Black', 'Won')
        sys.exit()

    def setup(self):
        # Place the rooks
        self.board[0][0] = Rook(False)
        self.board[0][7] = Rook(False)
        self.board[7][0] = Rook(True)
        self.board[7][7] = Rook(True)

        # Place the knights
        self.board[0][1] = Knight(False)
        self.board[0][6] = Knight(False)
        self.board[7][1] = Knight(True)
        self.board[7][6] = Knight(True)

        # Place the bishops
        self.board[0][2] = Bishop(False)
        self.board[0][5] = Bishop(False)
        self.board[7][2] = Bishop(True)
        self.board[7][5] = Bishop(True)

        # Place the queens
        self.board[0][3] = Queen(False)
        self.board[7][3] = Queen(True)

        # Place the kings
        self.board[0][4] = King(False)
        self.board[7][4] = King(True)

        # Place the pawns
        for i in range(8):
            self.board[1][i] = Pawn(False)
            self.board[6][i] = Pawn(True)
