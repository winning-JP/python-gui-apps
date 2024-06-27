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
bord = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

# 空欄の位置を保持するリスト
empty_cells = []


def update_empty_cells():
    global empty_cells
    empty_cells = [(row, col) for row in range(3)
                   for col in range(3) if bord[row][col] == " "]


def game(row, col, box):
    if bord[row][col] == " ":
        box.config(text="◯", font=("Arial", 24))
        bord[row][col] = "◯"
        update_empty_cells()
        print_bord()
        if empty_cells:
            ai_move()


def ai_move():
    if empty_cells:
        row, col = random.choice(empty_cells)
        bord[row][col] = "×"
        buttons[row][col].config(text="×", font=("Arial", 24))
        update_empty_cells()
        print_bord()


def print_bord():
    for row in range(3):
        for col in range(3):
            if bord[row][col] == "◯":
                print(f"◯ row: {row}, col: {col}")
            if bord[row][col] == " ":
                print(f"空欄 row: {row}, col: {col}")
            if bord[row][col] == "×":
                print(f"× row: {row}, col: {col}")
    if len(empty_cells) == 0:
        print("引き分け")
    else:
        num = random.randint(0, len(empty_cells)-1)
        print(empty_cells)
        print(f"ランダムに選ばれた空欄: {empty_cells[num]}")
    print()


# 初期化時に空欄の位置を更新
update_empty_cells()

# 入力フィールドの作成
label = tk.Label(window, text="マルバツゲーム", bg=bg_color,
                 fg=fg_color, font=("Arial", 18))
label.grid(row=0, column=0, columnspan=3, pady=10)

# ボタンの作成と配置
buttons = [[None, None, None], [None, None, None], [None, None, None]]

buttons[0][0] = tk.Button(window, text=" ", width=5, height=2, font=(
    "Arial", 24), command=lambda: game(0, 0, buttons[0][0]))
buttons[0][0].grid(row=1, column=0, padx=0, pady=0)
buttons[0][1] = tk.Button(window, text=" ", width=5, height=2, font=(
    "Arial", 24), command=lambda: game(0, 1, buttons[0][1]))
buttons[0][1].grid(row=1, column=1, padx=0, pady=0)
buttons[0][2] = tk.Button(window, text=" ", width=5, height=2, font=(
    "Arial", 24), command=lambda: game(0, 2, buttons[0][2]))
buttons[0][2].grid(row=1, column=2, padx=0, pady=0)

buttons[1][0] = tk.Button(window, text=" ", width=5, height=2, font=(
    "Arial", 24), command=lambda: game(1, 0, buttons[1][0]))
buttons[1][0].grid(row=2, column=0, padx=0, pady=0)
buttons[1][1] = tk.Button(window, text=" ", width=5, height=2, font=(
    "Arial", 24), command=lambda: game(1, 1, buttons[1][1]))
buttons[1][1].grid(row=2, column=1, padx=0, pady=0)
buttons[1][2] = tk.Button(window, text=" ", width=5, height=2, font=(
    "Arial", 24), command=lambda: game(1, 2, buttons[1][2]))
buttons[1][2].grid(row=2, column=2, padx=0, pady=0)

buttons[2][0] = tk.Button(window, text=" ", width=5, height=2, font=(
    "Arial", 24), command=lambda: game(2, 0, buttons[2][0]))
buttons[2][0].grid(row=3, column=0, padx=0, pady=0)
buttons[2][1] = tk.Button(window, text=" ", width=5, height=2, font=(
    "Arial", 24), command=lambda: game(2, 1, buttons[2][1]))
buttons[2][1].grid(row=3, column=1, padx=0, pady=0)
buttons[2][2] = tk.Button(window, text=" ", width=5, height=2, font=(
    "Arial", 24), command=lambda: game(2, 2, buttons[2][2]))
buttons[2][2].grid(row=3, column=2, padx=0, pady=0)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
