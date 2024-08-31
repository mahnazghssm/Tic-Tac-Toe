"""
Author: Mahnaz Ghassemi
Date created: 08,25,2024
Description: Tic Tac Toe
"""

import random


class TicTacToe:
    def __init__(self) -> None:
        """
        Initializes the game board with 10 empty spaces (index 0 is unused) 
        and randomly selects which player ('x' or 'o') will start the game.
        """
        self.board: list[str] = [" "] * 10  # A list of 10 strings representing the board cells.
        self.player_turn: str = self.get_random_first_player()  # Either 'x' or 'o' randomly selected.

    def get_random_first_player(self) -> str:
        """
        Randomly selects the first player (either 'x' or 'o') to start the game.
        
        Returns:
            str: Returns 'x' or 'o' as the first player.
        """
        return random.choice(["x", "o"])  # Randomly selects between 'x' and 'o'.
    
    def show_board(self) -> None:
        """
        Displays the current state of the Tic-Tac-Toe board in a 3x3 grid format.
        """
        print("\n")
        print(self.board[1] + "|" + self.board[2] + "|" + self.board[3])
        print("------")
        print(self.board[4] + "|" + self.board[5] + "|" + self.board[6])
        print("------")
        print(self.board[7] + "|" + self.board[8] + "|" + self.board[9])
        print("------")

    def swap_player_turn(self) -> None:
        """
        Swaps the turn to the other player. If the current player is 'x', it changes to 'o' and vice versa.
        """
        self.player_turn = "x" if self.player_turn == "o" else "o"

    def is_board_filled(self) -> bool:
        """
        Checks if all cells on the board are filled, indicating a draw.

        Returns:
            bool: Returns True if the board is completely filled, False otherwise.
        """
        return " " not in self.board[1:]  # Check if any empty spaces remain in the board (ignores index 0).
    
    def fix_spot(self, cell: int, player: str) -> None:
        """
        Assigns the player's mark ('x' or 'o') to the specified cell on the board.
        
        Args:
            cell (int): The board position (1-9) where the player wants to place their mark.
            player (str): The current player ('x' or 'o').
        """
        self.board[cell] = player

    def has_player_won(self, player: str) -> bool:
        """
        Checks if the current player has won by completing any of the winning combinations.
        
        Args:
            player (str): The player to check ('x' or 'o').
        
        Returns:
            bool: Returns True if the player has a winning combination, False otherwise.
        """
        # List of all possible winning combinations (rows, columns, and diagonals)
        win_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Horizontal rows
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Vertical columns
            [3, 5, 7], [1, 5, 9]              # Diagonals
        ]
        
        # Check if the player occupies all positions in any winning combination
        for combination in win_combinations:
            if all([self.board[cell] == player for cell in combination]):
                return True

        return False
    
    def start(self) -> None:
        """
        Starts the Tic-Tac-Toe game and runs until there is a winner or the game ends in a draw.
        The players take turns to place their mark on the board until a result is determined.
        """
        while True:
            self.show_board()  # Display the current board state
            print(f"Player {self.player_turn}'s turn")  # Inform which player's turn it is

            # Ask the player to select a valid cell (1-9)
            try:
                cell: int = int(input("Enter cell number from 1 to 9: "))  # Convert input to integer
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 9.")
                continue

            # Check if the selected cell is valid and empty
            if cell in range(1, 10) and self.board[cell] == " ":
                self.fix_spot(cell, self.player_turn)  # Mark the cell with the current player's mark

                # Check if the current player has won
                if self.has_player_won(self.player_turn):
                    self.show_board()
                    print(f"Player {self.player_turn} won!")
                    break

                # Check if the board is full (draw)
                if self.is_board_filled():
                    self.show_board()
                    print("It's a draw!")
                    break

                # Swap turn to the other player
                self.swap_player_turn()
            else:
                print("Invalid cell number! Please choose an empty cell between 1 and 9.")

# Entry point for running the game
if __name__ == "__main__":
    game = TicTacToe()
    game.start()