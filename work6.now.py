import tkinter as tk
import tkinter
import random

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)


table = [["", "", ""], ["", "", ""], ["", "", ""]]


if random.randint(0, 1) == 0:
    player_1 = "o"
    player_2 = "x"
else:
    player_1 = "x"
    player_2 = "o"
current_player = player_1


def button_action(x, y, button):
    # 自分の印をつける
    table[x][y] = player_1
    # 勝利判定
    if table[0][0] == table[0][1] == table[0][2] == player_1:
        label1.config(text="あなたの勝ちです")
    elif table[1][0] == table[1][1] == table[1][2] == player_1:
        label1.config(text="あなたの勝ちです")
    elif table[2][0] == table[2][1] == table[2][2] == player_1:
        label1.config(text="あなたの勝ちです")
    elif table[0][0] == table[1][0] == table[2][0] == player_1:
        label1.config(text="あなたの勝ちです")
    elif table[0][1] == table[1][1] == table[2][1] == player_1:
        label1.config(text="あなたの勝ちです")
    elif table[0][2] == table[1][2] == table[2][2] == player_1:
        label1.config(text="あなたの勝ちです")
    elif table[0][0] == table[1][1] == table[2][2] == player_1:
        label1.config(text="あなたの勝ちです")
    elif table[0][2] == table[1][1] == table[2][0] == player_1:
        label1.config(text="あなたの勝ちです")

    # コンピュータの印をつける
    x2 = 0
    y2 = 0
    for i, array in enumerate(table):
        for j, cell in enumerate(table):
            if cell == "":
                x2 = i
                y2 = j

    table[x2][y2] = player_2
    button.config(text=player_2)

    # コンピュータの勝利判定
    if table[0][0] == table[0][1] == table[0][2] == player_2:
        label1.config(text="コンピューターの勝ちです")
    elif table[1][0] == table[1][1] == table[1][2] == player_2:
        label1.config(text="コンピューターの勝ちです")
    elif table[2][0] == table[2][1] == table[2][2] == player_2:
        label1.config(text="コンピューターの勝ちです")
    elif table[0][0] == table[1][0] == table[2][0] == player_2:
        label1.config(text="コンピューターの勝ちです")
    elif table[0][1] == table[1][1] == table[2][1] == player_2:
        label1.config(text="コンピューターの勝ちです")
    elif table[0][2] == table[1][2] == table[2][2] == player_2:
        label1.config(text="コンピューターの勝ちです")
    elif table[0][0] == table[1][1] == table[2][2] == player_2:
        label1.config(text="コンピューターの勝ちです")
    elif table[0][2] == table[1][1] == table[2][0] == player_2:
        label1.config(text="コンピューターの勝ちです")


def button_action1():
    button1.config(text=player_1)
    button_action(0, 0, button1)


def button_action2():
    button2.config(text=player_1)
    button_action(0, 1, button2)


def button_action3():
    button3.config(text=player_1)
    button_action(0, 2)


def button_action4():
    button4.config(text=player_1)
    button_action(1, 0)


def button_action5():
    button5.config(text=player_1)
    button_action(1, 1)


def button_action6():
    button6.config(text=player_1)
    button_action(1, 2)


def button_action7():
    button7.config(text=player_1)
    button_action(2, 0)


def button_action8():
    button8.config(text=player_1)
    button_action(2, 1)


def button_action9():
    button9.config(text=player_1)
    button_action(2, 2)


button1 = tk.Button(window, text="", command=button_action1, width=3, height=3)
button1.pack(pady=10)
button1.place(x=200, y=100)
button2 = tk.Button(window, text="", command=button_action2, width=3, height=3)
button2.pack(pady=10)
button2.place(x=270, y=100)
button3 = tk.Button(window, text="", command=button_action3, width=3, height=3)
button3.pack(pady=10)
button3.place(x=340, y=100)
button4 = tk.Button(window, text="", command=button_action4, width=3, height=3)
button4.pack(pady=10)
button4.place(x=200, y=170)
button5 = tk.Button(window, text="", command=button_action5, width=3, height=3)
button5.pack(pady=10)
button5.place(x=270, y=170)
button6 = tk.Button(window, text="", command=button_action6, width=3, height=3)
button6.pack(pady=10)
button6.place(x=340, y=170)
button7 = tk.Button(window, text="", command=button_action7, width=3, height=3)
button7.pack(pady=10)
button7.place(x=200, y=240)
button8 = tk.Button(window, text="", command=button_action8, width=3, height=3)
button8.pack(pady=10)
button8.place(x=270, y=240)
button9 = tk.Button(window, text="", command=button_action9, width=3, height=3)
button9.pack(pady=10)
button9.place(x=340, y=240)


# 入力フィールドの作成

# ボタンの作成


# 出力ラベルの作成

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
