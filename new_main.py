import random

class TicTacToe:
    def __init__(self):
        self.board = [" "] * 10
        self.player_turn = self.get_random_first_player()
        self.user_symbol, self.computer_symbol = self.assign_symbols()

    def show_board(self):
        print("\n")
        print(self.board[1] + "|" + self.board[2] + "|" + self.board[3])
        print("-----")
        print(self.board[4] + "|" + self.board[5] + "|" + self.board[6])
        print("-----")
        print(self.board[7] + "|" + self.board[8] + "|" + self.board[9])
        print("-----")

    def get_random_first_player(self):
        return random.choice(["x", "o"])

    def assign_symbols(self):
        if random.choice(["user", "computer"]) == "user":
            print("🎲 You are randomly assigned as X.")
            return "x", "o"
        else:
            print("🎲 You are randomly assigned as O.")
            return "o", "x"

    def swap_player_turn(self):
        self.player_turn = "x" if self.player_turn == "o" else "o"

    def is_board_filled(self):
        return " " not in self.board[1:]

    def fix_spot(self, cell, player):
        self.board[cell] = player

    def has_player_won(self, player):
        win_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]
        ]
        for combo in win_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def start(self):
        while True:
            self.show_board()
            print(f"\n🎮 Player {self.player_turn}'s turn:")

            if self.player_turn == self.user_symbol:
                cell_input = input("Enter a number (1-9) or 'q' to quit: ").strip().lower()
                if cell_input == "q":
                    print("👋 Game quit. Thanks for playing!")
                    break
                try:
                    cell = int(cell_input)
                except ValueError:
                    print("❌ Invalid input. Please enter a number between 1 and 9 or 'q' to quit.")
                    continue
            else:
                available = [i for i in range(1, 10) if self.board[i] == " "]
                cell = random.choice(available)
                print(f"🤖 Computer chooses: {cell}")

            if cell in range(1, 10) and self.board[cell] == " ":
                self.fix_spot(cell, self.player_turn)

                if self.has_player_won(self.player_turn):
                    self.show_board()
                    if self.player_turn == self.user_symbol:
                        print("🎉 You win!")
                    else:
                        print("🤖 Computer wins!")
                    break

                if self.is_board_filled():
                    self.show_board()
                    print("🤝 It's a draw!")
                    break

                self.swap_player_turn()
            else:
                if self.player_turn == self.user_symbol:
                    print("⚠️ Invalid or occupied cell. Try again.")

# Run the game
if __name__ == "__main__":
    game = TicTacToe()
    game.start()