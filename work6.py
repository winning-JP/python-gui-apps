import tkinter as tk
import random

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("○×ゲーム")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

list = []


def game():
    #


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
