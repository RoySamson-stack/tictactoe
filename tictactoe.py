import tkinter as tk
from tkinter import messagebox;


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title = ("Tic Tac Toe")
        self.current_player = "X"
        self.board = [[""for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range (3)] for _ in range (3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.window, text="", font=("Helvetica", 24), width=5, height=5,
                    command=lambda row=i, col=j: self.on_button_click(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j)



    def on_button_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(row, col):
                messagebox.showinfo("Tic Tac Toe", f"PLayer {self.current_player} wins")
                self.reset()
            elif self.check_winner(row, col):
                messagebox.showinfo("Tic Tac Toe", "Its a tie")
                self.reset()
            else:
                self.current_player = "0" if  self.current_player  == "X" else "X"      
  



    def check_winner(self, row, col):
        if self.board[row].count(self.current_player) == 3:
             return True
        if [self.board[i][col] for i in range(3)].count(self.current_player) == 3:
            return True

        if row == col and [self.board[i][i] for i in range(3)].count(self.current_player) == 3:
            return True      
        if row + col == 2 and [self.board[i][2- i] for i in range(3)].count(self.current_player) == 3:
            return True

        return False        




    def check_tie(self):
        return all(all(cell != "" for cell in row ) for row in self.board)    



    def reset(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
                self.board[i][j] = ""
        self.current_player = "X"


    def run(self):
        self.window.mainloop()            



game = TicTacToe()
game.run()        