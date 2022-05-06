import random


class C4Game:
    ROWS = 6
    COLS = 7
    board = []
    nextPlayer = 'X'

    # Constructor initializes empty board with dots representing empty spaces
    def __init__(self):
        self.board = [['.' for c in range(self.COLS)]
                      for r in range(self.ROWS)]

    #
    def __str__(self):
        s = ""
        for row in range(self.ROWS):
            for col in range(self.COLS):
                s += self.board[row][col]
            s += "\n"
        return s[:-1]  # remove trailing newline and return

    # returns the set of legal moves given the current board configuration, i.e. all non-full columns
    def available_moves(self):
        return [c for c in range(self.COLS) if self.board[0][c] == '.']

    # Validates proposed move and places the next player's token in the column number specified.  Updates nextPlayer
    # accordingly
    # Returns True or False indicated whether move was accepted and performed
    def make_move(self, col):
        if col < 0 or col >= self.COLS:  # if out of range, not a valid move
            return False
        if self.board[0][col] != '.':  # if column is full, not a valid move
            return False
        row = self.ROWS - 1  # loop from bottom row up, looking for first open row to place token
        while self.board[row][col] != '.':
            row -= 1
        self.board[row][col] = self.nextPlayer

        # update nextPlayer to indicate whose turn is next
        if self.nextPlayer == 'X':
            self.nextPlayer = 'O'
        else:
            self.nextPlayer = 'X'

        return True

    # Detect a winner in the game -- either return 'X' or 'O' if one of them won, "stalemate" if board is full or
    # False if the game is not yet over.
    def winner(self):
        # check for horizonal wins
        for r in range(self.ROWS):
            for c in range(self.COLS-3):
                if self.board[r][c] != '.' and self.board[r][c] == self.board[r][c+1] and self.board[r][c] == self.board[r][c+2] and self.board[r][c] == self.board[r][c+3]:
                    return self.board[r][c]

        # check for vertical wins
        for r in range(self.ROWS-3):
            for c in range(self.COLS):
                if self.board[r][c] != '.' and self.board[r][c] == self.board[r+1][c] and self.board[r][c] == self.board[r+2][c] and self.board[r][c] == self.board[r+3][c]:
                    return self.board[r][c]

        # check for diagonal wins -- down right
        for r in range(self.ROWS-3):
            for c in range(self.COLS-3):
                if self.board[r][c] != '.' and self.board[r][c] == self.board[r+1][c+1] and self.board[r][c] == self.board[r+2][c+2] and self.board[r][c] == self.board[r+3][c+3]:
                    return self.board[r][c]

        # check for diagonal wins -- up right
        for r in range(3, self.ROWS):
            for c in range(self.COLS-3):
                if self.board[r][c] != '.' and self.board[r][c] == self.board[r-1][c+1] and self.board[r][c] == self.board[r-2][c+2] and self.board[r][c] == self.board[r-3][c+3]:
                    return self.board[r][c]

        # check for stalemate
        if self.available_moves():
            return False
        else:
            return "stalemate"
