# Tic-Tac-Toe in Python

A simple command-line Tic-Tac-Toe game for two players. Players take turns choosing a cell on a 3x3 board until one player wins or the game ends in a draw.

## Features

- Player vs Player (PvP) mode
- Randomly selects the starting player
- 3x3 game board
- Win and draw detection
- Handles invalid inputs

## How It Works

The `TicTacToe` class contains the main game logic.

- `get_random_first_player()`: randomly selects the first player
- `show_board()`: displays the current board
- `swap_player_turn()`: changes the turn to the other player
- `is_board_filled()`: checks if the board is full
- `fix_spot()`: places a player's mark on the board
- `has_player_won()`: checks for a winning combination
- `start()`: runs the game

## Project Structure

```text
.
├── .gitignore
├── README.md
└── src
    └── main.py
```

- `src/main.py`: contains the game class and logic
- `.gitignore`: files and folders ignored by Git
- `README.md`: project documentation

## Requirements

- Python 3.9 or later

No external packages are required.

## Running the Project

Run the game from the project root:

```bash
python src/main.py
```

## How to Play

The board uses numbers from 1 to 9 to represent each cell:

```text
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

Players take turns entering the number of an empty cell to place their mark.

For example:

```text
Player x's turn
Enter cell number from 1 to 9: 5
```

The game continues until one player wins or all cells are filled.

## Example

```text
Player x's turn
Enter cell number from 1 to 9: 5

 | | 
------
 |x| 
------
 | | 

Player o's turn
```
