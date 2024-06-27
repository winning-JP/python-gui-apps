import tkinter as tk

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


def game(row, col, box):
    box.config(text="◯", font=("Arial", 24))
    bord[row][col] = "◯"
    print_bord()


def print_bord():
    for row in range(3):
        for col in range(3):
            if bord[row][col] == "◯":
                print(f"(row: {row},col: {col})")
    print()


# 入力フィールドの作成
label = tk.Label(window, text="マルバツゲーム", bg=bg_color,
                 fg=fg_color, font=("Arial", 18))
label.grid(row=0, column=0, columnspan=3, pady=10)

# ボタンの作成と配置
box_0 = tk.Button(window, text=" ", width=5, height=2, font=(
    "Arial", 24), command=lambda: game(0, 0, box_0))
box_0.grid(row=1, column=0, padx=0, pady=0)
box_1 = tk.Button(window, text=" ", width=5, height=2, font=(
    "Arial", 24), command=lambda: game(0, 1, box_1))
box_1.grid(row=1, column=1, padx=0, pady=0)
box_2 = tk.Button(window, text=" ", width=5, height=2, font=(
    "Arial", 24), command=lambda: game(0, 2, box_2))
box_2.grid(row=1, column=2, padx=0, pady=0)

box_3 = tk.Button(window, text=" ", width=5, height=2, font=(
    "Arial", 24), command=lambda: game(1, 0, box_3))
box_3.grid(row=2, column=0, padx=0, pady=0)
box_4 = tk.Button(window, text=" ", width=5, height=2, font=(
    "Arial", 24), command=lambda: game(1, 1, box_4))
box_4.grid(row=2, column=1, padx=0, pady=0)
box_5 = tk.Button(window, text=" ", width=5, height=2, font=(
    "Arial", 24), command=lambda: game(1, 2, box_5))
box_5.grid(row=2, column=2, padx=0, pady=0)

box_6 = tk.Button(window, text=" ", width=5, height=2, font=(
    "Arial", 24), command=lambda: game(2, 0, box_6))
box_6.grid(row=3, column=0, padx=0, pady=0)
box_7 = tk.Button(window, text=" ", width=5, height=2, font=(
    "Arial", 24), command=lambda: game(2, 1, box_7))
box_7.grid(row=3, column=1, padx=0, pady=0)
box_8 = tk.Button(window, text=" ", width=5, height=2, font=(
    "Arial", 24), command=lambda: game(2, 2, box_8))
box_8.grid(row=3, column=2, padx=0, pady=0)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
