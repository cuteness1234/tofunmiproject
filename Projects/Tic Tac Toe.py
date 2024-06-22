import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text=" ", font=("Helvetica", 24), height=2, width=5,
                                command=lambda row=i, col=j: self.make_move(row, col))
                btn.grid(row=i, column=j)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.update_button(row, col)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.root.quit()
            elif all(cell != " " for row in self.board for cell in row):
                messagebox.showinfo("Game Over", "It's a tie!")
                self.root.quit()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def update_button(self, row, col):
        btn = self.root.grid_slaves(row=row, column=col)[0]
        btn.config(text=self.board[row][col], state=tk.DISABLED)

    def check_winner(self):
        for i in range(3):
            if all(cell == self.current_player for cell in self.board[i]) or \
               all(self.board[j][i] == self.current_player for j in range(3)):
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player or \
           self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player:
            return True
        return False

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
