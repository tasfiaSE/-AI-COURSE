import tkinter as tk
from tkinter import messagebox
import copy

# Constants
PLAYER = 'X'
AI = 'O'
EMPTY = ''
GAME_OVER = False

# Colors
COLOR_BLUE = "#4584b6"
COLOR_YELLOW = "#ffde57"
COLOR_GRAY = "#343434"
COLOR_LIGHT_GRAY = "#646464"

# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe with AI")
root.resizable(False, False)

# Label to display game status
label = tk.Label(root, text="Your Turn (X)", font=("Consolas", 20), background=COLOR_GRAY, foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

# Initialize board
buttons = [[None for _ in range(3)] for _ in range(3)]
board = [[EMPTY for _ in range(3)] for _ in range(3)]

def check_winner(b):
    # Check rows and columns
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != EMPTY:
            return b[i][0]
        if b[0][i] == b[1][i] == b[2][i] != EMPTY:
            return b[0][i]
    # Check diagonals
    if b[0][0] == b[1][1] == b[2][2] != EMPTY:
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != EMPTY:
        return b[0][2]
    return None

def is_full(b):
    for row in b:
        if EMPTY in row:
            return False
    return True

def minimax(b, depth, is_maximizing):
    winner = check_winner(b)
    if winner == AI:
        return 1
    elif winner == PLAYER:
        return -1
    elif is_full(b):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if b[i][j] == EMPTY:
                    b[i][j] = AI
                    score = minimax(b, depth + 1, False)
                    b[i][j] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if b[i][j] == EMPTY:
                    b[i][j] = PLAYER
                    score = minimax(b, depth + 1, True)
                    b[i][j] = EMPTY
                    best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                score = minimax(board, 0, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        i, j = move
        board[i][j] = AI
        buttons[i][j]['text'] = AI
        buttons[i][j]['fg'] = COLOR_YELLOW
        winner = check_winner(board)
        if winner:
            label.config(text=f"{winner} wins!", foreground=COLOR_YELLOW)
            global GAME_OVER
            GAME_OVER = True
        elif is_full(board):
            label.config(text="Draw!", foreground=COLOR_YELLOW)
            GAME_OVER = True
        else:
            label.config(text="Your Turn (X)", foreground="white")

def on_click(i, j):
    global GAME_OVER
    if GAME_OVER or board[i][j] != EMPTY:
        return
    board[i][j] = PLAYER
    buttons[i][j]['text'] = PLAYER
    buttons[i][j]['fg'] = COLOR_BLUE
    winner = check_winner(board)
    if winner:
        label.config(text=f"{winner} wins!", foreground=COLOR_YELLOW)
        GAME_OVER = True
    elif is_full(board):
        label.config(text="Draw!", foreground=COLOR_YELLOW)
        GAME_OVER = True
    else:
        label.config(text="Computer's Turn (O)", foreground="white")
        root.after(500, ai_move)

def reset_game():
    global board, GAME_OVER
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j]['text'] = EMPTY
            buttons[i][j]['fg'] = COLOR_BLUE
            buttons[i][j]['bg'] = COLOR_GRAY
    label.config(text="Your Turn (X)", foreground="white")
    GAME_OVER = False

# Create buttons for the board
for i in range(3):
    for j in range(3):
        button = tk.Button(root, text=EMPTY, font=("Consolas", 40), width=5, height=2,
                           bg=COLOR_GRAY, fg=COLOR_BLUE,
                           command=lambda i=i, j=j: on_click(i, j))
        button.grid(row=i+1, column=j)
        buttons[i][j] = button

# Reset button
reset_button = tk.Button(root, text="New Game", font=("Consolas", 20), bg=COLOR_GRAY,
                         fg="white", command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3, sticky="we")

root.mainloop()

