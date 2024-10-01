import tkinter as tk
from tkinter import messagebox
import math

board = [' ' for _ in range(9)]

def check_winner(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]  # Diagonal
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def empty_spaces():
    return ' ' in board

def minimax(board, is_maximizing):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if not empty_spaces():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'
    buttons[move].config(text='O', state='disabled')
    check_game_over()

def user_move(index):
    if board[index] == ' ':
        board[index] = 'X'
        buttons[index].config(text='X', state='disabled')
        check_game_over()
        if empty_spaces():
            ai_move()

def check_game_over():
    if check_winner('X'):
        messagebox.showinfo("Game Over", "You win!")
        reset_game()
    elif check_winner('O'):
        messagebox.showinfo("Game Over", "AI wins!")
        reset_game()
    elif not empty_spaces():
        messagebox.showinfo("Game Over", "It's a tie!")
        reset_game()

def reset_game():
    global board
    board = [' ' for _ in range(9)]
    for button in buttons:
        button.config(text='', state='normal')

window = tk.Tk()
window.title("Tic-Tac-Toe AI")

buttons = []
for i in range(9):
    button = tk.Button(window, text='', font='Helvetica 20', height=3, width=6,
                       command=lambda i=i: user_move(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

reset_button = tk.Button(window, text="Reset Game", font='Helvetica 14', command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

window.mainloop()
