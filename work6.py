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

def print_bord():
    for row in range(3):
        for col in range(3):
            if bord[row][col] == "❌":
                print(f"(row: {row},col: {col})")
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


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # 行をチェック
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # 列をチェック
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # 対角線をチェック
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter the row (0, 1, 2): "))
        col = int(input(f"Player {current_player}, enter the column (0, 1, 2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("The cell is already occupied. Try again.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
