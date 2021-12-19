import random
from connect_four import Connect4

def importBots():
    bot_a_name = input("Name of bot A: ")
    bot_b_name = input("Name of bot B: ")

    globals()["BotA"] = getattr(__import__(bot_a_name), bot_a_name)
    globals()["BotB"] = getattr(__import__(bot_b_name), bot_b_name)

def main():
    importBots()

    board = Connect4()

    if random.randint(0, 1) == 0:
        print(f"{BotA.getName(BotA)} will go first!")
        FirstBot = BotA
        SecondBot = BotB
    else:
        print(f"{BotB.getName(BotB)} will go first!")
        FirstBot = BotB
        SecondBot = BotA

    while True:
        if board.hasWon() == 0: takeTurn(FirstBot, board, 1)
        else: break
        if board.hasWon() == 0: takeTurn(SecondBot, board, 2)
        else: break

def takeTurn(bot, board, player):
    column = bot.chooseColumn(bot, board)
    board.dropPiece(player, column)

    if board.hasWon() == 4:
        print(f"Draw!")
        print("Final board:")
        print(board)
    elif board.hasWon() != 0:
        print(f"{bot.getName(bot)} won!")
        print(f"{bot.getName(bot)} says: {bot.winMessage(bot)}")
        print("Final board:")
        print(board)

if __name__ == "__main__":
    main()
