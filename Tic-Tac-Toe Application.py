import tkinter as tk
from tkinter import messagebox

# Initialize the game state
current_player = "X"
board = [" " for _ in range(9)]

def check_win(player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def check_tie():
    return " " not in board

def on_button_click(button):
    global current_player

    if board[button] == " ":
        board[button] = current_player
        buttons[button].config(text=current_player)
        
        if check_win(current_player):
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            reset_game()
        elif check_tie():
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_game():
    global current_player, board
    current_player = "X"
    board = [" " for _ in range(9)]

    for button in buttons:
        button.config(text=" ")
        button.config(state=tk.NORMAL)

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create buttons for the game board
buttons = [tk.Button(root, text=" ", font=("normal", 20), width=8, height=4, command=lambda i=i: on_button_click(i)) for i in range(9)]
for i, button in enumerate(buttons):
    row, col = i // 3, i % 3
    button.grid(row=row, column=col)

# Create a "Reset" button
reset_button = tk.Button(root, text="Reset", font=("normal", 20), command=reset_game)
reset_button.grid(row=3, column=1)

root.mainloop()
