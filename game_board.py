class Board():
    def __init__(self, rows=3, columns=3):
        self.__rows = int(rows)
        self.__columns = int(columns)
        self.__board = [[0]*self.__columns for _ in range(self.__rows)]

    def getBoard(self):
        return self.__board.copy()

    def getPosition(self, column, row):
        return self.getBoard()[row][column]

    def check(self, how_many_in_a_line, column, row, column_change=0, row_change=0):
        n = self.getPosition(column, row)
        return n if (n != 0 and all(self.getPosition(column + i * column_change, row + i * row_change) == n for i in range(how_many_in_a_line))) else False

    def hasWon(self, how_many_in_a_line):
        num_of_row_checks = self.numOfRows() - how_many_in_a_line + 1
        num_of_column_checks = self.numOfColumns() - how_many_in_a_line + 1

        # Check for a horizontal line
        for row in range(self.numOfRows()):
            for column in range(num_of_column_checks):
                if n := self.check(how_many_in_a_line, column, row, 1, 0): return n

        # Check for a vertical line
        for column in range(self.numOfColumns()):
            for row in range(num_of_row_checks):
                if n := self.check(how_many_in_a_line, column, row, 0, 1): return n

        # Check for a diagonal line
        for column in range(num_of_column_checks):
            for row in range(num_of_row_checks):
                if n := self.check(how_many_in_a_line, column, row, 1, 1): return n
                if n := self.check(how_many_in_a_line, self.numOfColumns() - column - 1, row, -1, 1): return n

        # Check if there is an empty space
        for row in self.getBoard():
            if 0 in row: # There is an empty space, so no winner yet
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
