import random
from bot import Bot

class TestBot(Bot):
    def __init__(self):
        pass

    def chooseColumn(self, board):
        # Pick a random valid move
        return random.choice([c for c in range(board.numOfColumns()) if board.isValidMove(c)])

    def getName(self):
        return "TestBot"

    def winMessage(self):
        return "Victory!"
