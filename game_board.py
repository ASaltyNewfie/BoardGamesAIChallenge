class Board():
    def __init__(self, rows=3, columns=3):
        self.__rows = int(rows)
        self.__columns = int(columns)
        self.__board = [[0]*self.__columns for _ in range(self.__rows)]

    def getBoard(self):
        return self.__board.copy()

    def getPosition(self, column, row):
        return self.getBoard()[row][column]

    def hasWon(self, how_many_in_a_line):
        # Check for a horizontal line
        for row in range(self.numOfRows()):
            for column in range(self.numOfColumns() - how_many_in_a_line + 1):
                if (n := self.getPosition(column, row)) != 0:
                    valid = True
                    for i in range(how_many_in_a_line):
                        if self.getPosition(column + i, row) != n:
                            valid = False
                    if valid:
                        return n

        # Check for a vertical line
        for column in range(self.numOfColumns()):
            for row in range(self.numOfRows() - how_many_in_a_line + 1):
                if (n := self.getPosition(column, row)) != 0:
                    valid = True
                    for i in range(how_many_in_a_line):
                        if self.getPosition(column, row + i) != n:
                            valid = False
                    if valid:
                        return n

        # Check for a diagonal line
        for column in range(self.numOfColumns() - how_many_in_a_line + 1):
            for row in range(self.numOfRows() - how_many_in_a_line + 1):
                if (n := self.getPosition(column, row)) != 0:
                    valid = True
                    for i in range(how_many_in_a_line):
                        if self.getPosition(column + i, row + i) != n:
                            valid = False
                    if valid:
                        return n

                inverse_column = self.numOfColumns() - column - 1
                if (n := self.getPosition(inverse_column, row)) != 0:
                    valid = True
                    for i in range(how_many_in_a_line):
                        if self.getPosition(inverse_column - i, row + i) != n:
                            valid = False
                    if valid:
                        return n

        # Check if there is an empty space
        for column in range(self.numOfColumns()):
            for row in range(self.numOfRows()):
                if self.getPosition(column, row) == 0: # There is an empty space, so no winner yet
                    return 0

        # There are no empty spaces, and no winner, so the game is a draw
        return 4

    def isValidMove(self, column, row):
        return self.getPosition(column, row) == 0

    def numOfColumns(self):
        return self.__columns

    def numOfRows(self):
        return self.__rows

    def takeMove(self, player, column, row):
        self.__board[row][column] = player

    def __str__(self):
        return "\n".join([str(row)[1:-1] for row in self.getBoard()])
