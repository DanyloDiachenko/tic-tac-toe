import tkinter as tk
from tkinter import messagebox

# Глобальні змінні
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]

# Функція для обробки кліків на кнопки
def button_click(row, col):
    global current_player

    if board[row][col] == "" and current_player != "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        if check_winner(row, col):
            messagebox.showinfo("Гра закінчена", f"Гравець {current_player} переміг!")
            reset_board()
        elif is_board_full():
            messagebox.showinfo("Гра закінчена", "Нічия!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"

# Перевірка на переможця
def check_winner(row, col):
    return (check_row(row) or check_column(col) or check_diagonals())

def check_row(row):
    return all(board[row][col] == current_player for col in range(3))

def check_column(col):
    return all(board[row][col] == current_player for row in range(3))

def check_diagonals():
    return (board[0][0] == board[1][1] == board[2][2] == current_player or
            board[0][2] == board[1][1] == board[2][0] == current_player)

# Перевірка на нічию
def is_board_full():
    return all(all(cell != "" for cell in row) for row in board)

# Скидання дошки для нової гри
def reset_board():
    global current_player, board
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", state="active")

# Створення вікна
root = tk.Tk()
root.title("Хрестики-нулики")

# Створення кнопок для гри
buttons = [[None, None, None] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", font=("Arial", 24), width=6, height=3,
                                      command=lambda row=row, col=col: button_click(row, col))
        buttons[row][col].grid(row=row, column=col)

# Початок гри
root.mainloop()
