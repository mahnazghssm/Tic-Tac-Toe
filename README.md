# Tic-Tac-Toe in Python

This is a simple command-line implementation of the classic Tic-Tac-Toe game using Python. Two players (Player `X` and Player `O`) take turns to play the game, and the game can end with a win for one player or a draw if no more moves are possible.

## Features
- Randomized starting player (`X` or `O`)
- Player vs Player (PvP) mode
- Board updates in real-time after every move
- Win and draw detection
- Simple and intuitive gameplay

## Rules
- The game is played on a 3x3 grid.
- Players take turns to place their symbol (`X` or `O`) in an empty cell.
- The first player to get 3 of their symbols in a row (horizontally, vertically, or diagonally) wins.
- If all 9 cells are filled and no player has won, the game ends in a draw.

## Requirements
- Python 3.x

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/your-username/tic-tac-toe.git
    ```

2. Navigate to the project directory:
    ```bash
    cd tic-tac-toe
    ```

3. Run the Python script:
    ```bash
    python3 tictactoe.py
    ```

## How to Play

- The game will prompt the player to choose a cell numbered 1 to 9, where each number represents a position on the board:
```
1 | 2 | 3

4 | 5 | 6

7 | 8 | 9
```
- The game will inform you which player's turn it is (`X` or `O`).
- Players input a number to place their symbol in the corresponding cell.

Example:
```
Player x turn
Enter cell number from 1 to 9: 5
```
- The board updates after each turn.
- The game will continue until one player wins or the game ends in a draw.

## Example Game Output
| |

| |

| |

Player x turn
Enter cell number from 1 to 9: 5
| |

|x|

| |


## Future Improvements
- Add a computer vs player mode with basic AI.
- Add error handling for invalid inputs (non-integer values).
- Improve the command-line interface with colors and better formatting.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Feel free to contribute by creating issues or submitting pull requests!


