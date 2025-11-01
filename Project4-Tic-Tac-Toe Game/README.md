# Tic-Tac-Toe Game

This is a simple command-line Tic-Tac-Toe game implemented in Python using NumPy.

# Features

* Two players: Human (X) vs Computer (O)
* Computer can block player’s winning moves and try to win
* Checks for win conditions (rows, columns, main and secondary diagonals)
* Detects draw situations when the board is full
* Input validation for player moves

# How to Play

* The board positions are numbered from 1 to 9 .
* Enter the number corresponding to the cell where you want to place your 'X'.
* The computer will automatically place its 'O'.
* The game ends when either player wins or the board is full (draw).

# Optional: Easier Computer Mode

If you want to make the game easier, you can disable the computer’s blocking and winning strategy.
In this mode, the computer will choose a random empty cell instead of trying to block or win.

To enable this mode, modify the 'computer_move' function in the code by removing or commenting out the parts that check for winning or blocking moves.
This will make the computer play randomly and make the game easier for the player.
