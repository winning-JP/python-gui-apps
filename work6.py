import tkinter as tk
# import random

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("○×ゲーム")
window.geometry("165x160")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

# ボードの状態を保持するリスト
board = [[None for _ in range(3)] for _ in range(3)]


def game(row, col):
    button = board[row][col]
    button.config(text="◯")


# 入力フィールドの作成
label = tk.Label(window, text="マルバツゲーム", bg=bg_color, fg=fg_color)
label.grid(row=0, column=0, columnspan=3)

# ボタンの作成
for row in range(3):
    for col in range(3):
        button = tk.Button(
            window, text=" ", command=lambda row=row, col=col: game(row, col), width=2, height=2)
        button.grid(row=row+1, column=col)
        board[row][col] = button

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
