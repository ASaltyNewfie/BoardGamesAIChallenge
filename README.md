
# BoardGamesAIChallenge

## init.py

Runs an instance of a Connect 4 game. The two inputs are the names of the corresponding bot
files without the .py extension.

**Example output:**

Name of bot A: TestBot\
Name of bot B: TestBot2\
TestBot2 will go first!\
TestBot2 won!\
TestBot2 says: Hahaha!\
Final board:\
0, 0, 0, 0, 0, 0, 0\
0, 0, 0, 0, 0, 0, 0\
0, 0, 0, 1, 0, 0, 0\
0, 1, 2, 1, 0, 2, 0\
2, 2, 2, 1, 2, 1, 1\
1, 1, 2, 1, 1, 2, 2

## game_board.py

Defines the `Board` class.

| Function | Description |
| ----------- | ----------- |
| getBoard() | Returns a copy of the internal board array. Not recommended for use by bots, use `getPosition()` instead. |
| getPosition(column, row) | Returns the value at the position. Position can be 0 (empty), 1, or 2. |
| hasWon(how_many_in_a_line) | Checks if a player has completed a line of the length specified. Returns 0 if there is no winner, or 4 if there is a draw. |
| isValidMove(column, row) | Implemented by child classes. |
| numOfColumns() | Self-explanatory. |
| numofRows() | Self-explanatory. |
| takeMove(player, column, row) | Places a piece of the player on the position. Only method which modifies the internal board. |

## connect_four.py

Defines the `Connect4` class.

| Function | Description |
| ----------- | ----------- |
| dropPiece(player, column) | Drop the players piece into the specified column. Raises an error if the move is invalid. |
| hasWon() | Calls the super function but specifies a line of length 4. |
| isValidMove(column) | Checks that the column exists (a board with 7 columns will return false if 'column' is 9 or -1) and that it is not full.|

## bot.py

Defines the `Bot` class, which serves as the base for all other bots.

| Function | Description |
| ----------- | ----------- |
| chooseColumn(board) | Given a `Board` object, return the column where the bot would like to place a piece. |
| getName() | The name the bot would like to be called. |
| winMessage() | The phrase the bot says when it wins (gloating encouraged). |

## TestBot.py / TestBot2.py

Defines the `TestBot` and `TestBot2` classes, which pick random valid moves. Useful for\
testing the engine
