import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("名簿作成")
window.geometry("600x400")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
names = []
# ↑↑↑ お約束のコード ↑↑↑


def name():
    name_out = ""
    names.append(entry1.get())
    for i in names:
        name_out += f"{i}\n"
    label1.config(text=f"{name_out}\n")


# ウィジェットの作成
label2 = tk.Label(window, text="名前を入力してください", bg=bg_color, fg=fg_color)
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
button1 = tk.Button(window, text="追加", command=name)
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)


# ウィジェットの配置
label2.pack()
entry1.pack(pady=10)
button1.pack(pady=10)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
