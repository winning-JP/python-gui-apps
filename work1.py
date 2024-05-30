import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("電卓")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑


def calculator_1():
    num1 = entry1.get()
    num2 = entry2.get()
    label1.config(text=f"{num1} + {num2} = {int(num1)+int(num2)}")


def calculator_2():
    num1 = entry1.get()
    num2 = entry2.get()
    label1.config(text=f"{num1} - {num2} = {int(num1)-int(num2)}")


def calculator_3():
    num1 = entry1.get()
    num2 = entry2.get()
    label1.config(text=int(num1)*int(num2))
    label1.config(text=f"{num1} x {num2} = {int(num1)*int(num2)}")


def calculator_4():
    num1 = entry1.get()
    num2 = entry2.get()
    label1.config(text=int(num1)/int(num2))
    label1.config(text=f"{num1} ÷ {num2} = {int(num1)/int(num2)}")


# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)

entry1.pack(pady=10)

entry2 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry2.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="+", command=calculator_1)
button1.pack(pady=10)

button2 = tk.Button(window, text="-", command=calculator_2)
button2.pack(pady=10)

button3 = tk.Button(window, text="x", command=calculator_3)
button3.pack(pady=10)

button4 = tk.Button(window, text="÷", command=calculator_4)
button4.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
