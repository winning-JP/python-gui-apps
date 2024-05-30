import tkinter as tk
import random

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("名簿作成&ランダム")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
names = []
# ↑↑↑ お約束のコード ↑↑↑


def name():
    name = entry1.get()
    if name == "":
        label1.config(text="名前を入力してください。")
    else:
        names.append(name)
        name_out = ""
        for i in names:
            name_out += f"{i}\n"
        label1.config(text=f"{name_out}\n")


def select():
    if len(names) == 0:
        label2.config(text="名前が登録されていません。")
    else:
        num = random.randint(0, len(names)-1)
        label2.config(text=f"{names[num]}")


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)


# ボタンの作成
button1 = tk.Button(window, text="追加", command=name)
button1.pack(pady=10)

button2 = tk.Button(window, text="ランダム選択", command=select)
button2.pack(pady=10)


# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

label2 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label2.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
