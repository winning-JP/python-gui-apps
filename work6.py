import tkinter as tk
# import random

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("○×ゲーム")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


def game(box):

    # 入力フィールドの作成
label = tk.Label(window, text="マルバツゲーム", bg=bg_color, fg=fg_color)
label.grid(row=0, column=0)

# ボタンの作成
box_0 = tk.Button(window, text=" ", command=game(0))
box_0.grid(row=2, column=1)
box_1 = tk.Button(window, text=" ")
box_1.grid(row=2, column=2)
box_2 = tk.Button(window, text=" ")
box_2.grid(row=2, column=3)

box_3 = tk.Button(window, text=" ")
box_3.grid(row=3, column=1)
box_4 = tk.Button(window, text=" ")
box_4.grid(row=3, column=2)
box_5 = tk.Button(window, text=" ")
box_5.grid(row=3, column=3)

box_6 = tk.Button(window, text=" ")
box_6.grid(row=4, column=1)
box_7 = tk.Button(window, text=" ")
box_7.grid(row=4, column=2)
box_8 = tk.Button(window, text=" ")
box_8.grid(row=4, column=3)


# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
