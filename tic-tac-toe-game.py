import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.resizable(False, False)
        
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        
        self.create_board()
        
    def create_board(self):
        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(self.root, text=" ", font=("Helvetica", 32), 
                                   width=3, height=1, command=lambda row=row, col=col: self.button_click(row, col))
                button.grid(row=row, column=col, sticky="nsew")
                button_row.append(button)
                
            self.buttons.append(button_row)
            
        restart_button = tk.Button(self.root, text="Restart", font=("Helvetica", 16), 
                                    width=10, height=1, command=self.restart_game)
        restart_button.grid(row=3, column=0, columnspan=3, sticky="nsew")
        
    def button_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_win():
                self.show_win_message()
            elif self.check_tie():
                self.show_tie_message()
            else:
                self.switch_player()
    
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False
    
    def check_tie(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == " ":
                    return False
        return True
    
    def show_win_message(self):
        messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
        self.restart_game()
    
    def show_tie_message(self):
        messagebox.showinfo("Game Over", "Tie!")
        self.restart_game()
        
    def restart_game(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for button in row:
                button.config(text=" ")
    
    def start_game(self):
        self.root.mainloop()
        
if __name__ == "__main__":
    game = TicTacToe()
    game.start_game()

    