import tkinter as tk
import random

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("タイピングアプリ")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

str_list = ["明日は雨", "今日はいい天気"]

num = random.randint(0, len(str_list)-1)
text = str_list[num]


def typing():
    global num, text
    if text == type_entry.get():
        num = random.randint(0, len(str_list)-1)
        text = str_list[num]
        label1.config(text=text)
        type_entry.delete(0, tk.END)


# 入力フィールドの作成
label1 = tk.Label(window, text=text, bg=bg_color, fg=fg_color)
label1.pack(pady=10)

type_entry = tk.Entry(window, bg=fg_color, fg=bg_color)
type_entry.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="OK", command=typing)
button1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
