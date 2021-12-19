from game_board import Board

class Connect4(Board):
    def __init__(self):
        super().__init__(6, 7)

    def dropPiece(self, player, column):
        if not self.isValidMove(column):
            raise Exception(f"Dropping a piece into column {column} is an invalid move")

        for row in range(1, self.numOfRows()):
            if self.getPosition(column, row) != 0:
                self.takeMove(player, column, row - 1)
                return

        self.takeMove(player, column, self.numOfRows() - 1)

    def hasWon(self):
        return super().hasWon(4)

    def isValidMove(self, column):
        if 0 > column or column >= self.numOfColumns(): # The column is outside the bounds of the board
            return False

        if self.getBoard()[0][column] != 0: # The column is full
            return False

        return True
