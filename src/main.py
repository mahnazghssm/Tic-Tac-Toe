"""
Author: Mahnaz Ghassemi
Date created: 08,25,2024
Description: Tic Tac Toe
"""

import random


class TicTacToe:
    def __init__(self) -> None:
        self.board: list[str] = [" "] * 10
        self.player_turn: str = self.get_random_first_player()

    def get_random_first_player(self) -> str:
        return random.choice(["x", "o"])

    def show_board(self) -> None:
        print("\n")
        print(self.board[1] + "|" + self.board[2] + "|" + self.board[3])
        print("------")
        print(self.board[4] + "|" + self.board[5] + "|" + self.board[6])
        print("------")
        print(self.board[7] + "|" + self.board[8] + "|" + self.board[9])
        print("------")

    def swap_player_turn(self) -> None:
        self.player_turn = "x" if self.player_turn == "o" else "o"

    def is_board_filled(self) -> bool:
        return " " not in self.board[1:]

    def fix_spot(self, cell: int, player: str) -> None:
        self.board[cell] = player

    def has_player_won(self, player: str) -> bool:
        win_combinations = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [3, 5, 7],
            [1, 5, 9]
        ]

        for combination in win_combinations:
            if all(self.board[cell] == player for cell in combination):
                return True

        return False

    def start(self) -> None:
        while True:
            self.show_board()
            print(f"Player {self.player_turn}'s turn")

            try:
                cell: int = int(input("Enter cell number from 1 to 9: "))
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 9.")
                continue

            if cell in range(1, 10) and self.board[cell] == " ":
                self.fix_spot(cell, self.player_turn)

                if self.has_player_won(self.player_turn):
                    self.show_board()
                    print(f"Player {self.player_turn} won!")
                    break

                if self.is_board_filled():
                    self.show_board()
                    print("It's a draw!")
                    break

                self.swap_player_turn()
            else:
                print(
                    "Invalid cell number! "
                    "Please choose an empty cell between 1 and 9."
                )


if __name__ == "__main__":
    game = TicTacToe()
    game.start()
