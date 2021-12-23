import numpy as np

class Board():
    def __init__(self, rows=3, columns=3):
        self.__rows = int(rows)
        self.__columns = int(columns)
        self.__board = [[0]*self.__columns for _ in range(self.__rows)]

    def getBoard(self):
        return self.__board.copy()

    def getPosition(self, column, row):
        return self.getBoard()[row][column]

    def hasWon(self, line_size):
        board = np.array(self.getBoard())
        slices = []

        # Horizontal lines
        slices += [row for row in board]

        # Vertical lines
        slices += [column for column in np.rot90(board)]

        # Diagonal lines
        slices += [board[::-1,:].diagonal(i) for i in range(-self.numOfRows()+1, self.numOfColumns())]
        slices += [board.diagonal(i) for i in range(self.numOfColumns()-1, -self.numOfRows(), -1)]

        for slice in slices:
            for i in range(len(slice)-line_size+1):
                p = slice[i]
                if p > 0 and all(n==p for n in slice[i:i+line_size]):
                    return p

        if 0 in board: return -1
        else: return 0

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
