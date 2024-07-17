import tkinter as tk
import random

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("○×ゲーム")
window.geometry("320x255")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

# ボードの状態を保持するリスト
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, mark):
    # 行のチェック
    for row in board:
        if all(s == mark for s in row):
            return True

    # 列のチェック
    for col in range(3):
        if all(row[col] == mark for row in board):
            return True

    # 斜めのチェック
    if all(board[i][i] == mark for i in range(3)):
        return True
    if all(board[i][2 - i] == mark for i in range(3)):
        return True

    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "⭕️"
    move_count = 0

    while move_count < 9:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if board[row][col] != " ":
            print("Cell already taken! Try again.")
            continue

        board[row][col] = current_player
        move_count += 1

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return

        current_player = "❌" if current_player == "⭕️" else "⭕️"

    print_board(board)
    print("It's a draw!")

tic_tac_toe()

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
