import tkinter as tk
# import random
import pygame

# 初期設定
window = tk.Tk()
window.title("○×ゲーム")
window.geometry("320x350")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)

# ボードの状態を保持するリスト
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

# 空欄の位置を保持するリスト
empty_cells = []


def play_victory_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("victory_sound.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()


def play_lose_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("lose_sound.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()


def play_dorow_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("dorow_sound.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()


def update_empty_cells():
    global empty_cells
    empty_cells = [(row, col) for row in range(3)
                   for col in range(3) if board[row][col] == " "]

# 勝敗を判定する関数


def check_winner():
    # 勝利条件の組み合わせをリストにする
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    # 勝利条件をチェック
    for condition in win_conditions:
        if board[condition[0][0]][condition[0][1]] == board[condition[1][0]][condition[1][1]] == board[condition[2][0]][condition[2][1]] != " ":
            return board[condition[0][0]][condition[0][1]]
    # 引き分け判定
    if not empty_cells:
        return "Draw"
    return None

# 勝敗判定後の処理


def end_game(result):
    if result == "◯":
        play_victory_sound()
        result_text = "あなたの勝ちです！"
    elif result == "✘":
        play_lose_sound()()
        result_text = "コンピュータの勝ちです。"
    elif result == "Draw":
        play_dorow_sound()()
        result_text = "引き分けです。"
    # 結果を表示するラベルを作成
    result_label = tk.Label(window, text=result_text, bg=bg_color,
                            fg=fg_color, font=("Arial", 18))
    result_label.grid(row=4, column=0, columnspan=3, pady=10)
    # 全てのボタンを無効化
    for row in buttons:
        for button in row:
            button.config(state="disabled")

# プレイヤーのターン


def game(row, col, box):
    if board[row][col] == " ":
        box.config(text="◯", font=("Arial", 24))
        board[row][col] = "◯"
        update_empty_cells()
        result = check_winner()
        if result:
            end_game(result)
        else:
            if empty_cells:
                ai_move()

# AIのターン（ミニマックスアルゴリズム）


def ai_move():
    if empty_cells:
        best_score = -float("inf")
        best_move = None
        for row, col in empty_cells:
            board[row][col] = "✘"
            score = minimax(board, False)
            board[row][col] = " "
            if score > best_score:
                best_score = score
                best_move = (row, col)
        if best_move:
            row, col = best_move
            board[row][col] = "✘"
            buttons[row][col].config(text="✘", font=("Arial", 24))
            update_empty_cells()
            result = check_winner()
            if result:
                end_game(result)

# ミニマックスアルゴリズム


def minimax(board, is_maximizing):
    result = check_winner()
    if result == "✘":
        return 1
    elif result == "◯":
        return -1
    elif result == "Draw":
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "✘"
                    score = minimax(board, False)
                    board[row][col] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "◯"
                    score = minimax(board, True)
                    board[row][col] = " "
                    best_score = min(score, best_score)
        return best_score

# ゲームをリセットする関数


def reset_game():
    global board, empty_cells
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    update_empty_cells()
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=" ", state="normal")
    # 既存の結果ラベルがある場合、削除する
    for widget in window.grid_slaves():
        if int(widget.grid_info()["row"]) == 4:
            widget.grid_forget()

# 現在のボードの状態を出力


def print_board():
    for row in range(3):
        for col in range(3):
            print(f"{board[row][col]} (row: {row}, col: {col})")
    if not empty_cells:
        print("引き分け")
    print()


# 初期化時に空欄の位置を更新
update_empty_cells()

# ラベルの作成
label = tk.Label(window, text="マルバツゲーム", bg=bg_color,
                 fg=fg_color, font=("Arial", 18))
label.grid(row=0, column=0, columnspan=3, pady=10)

# ボタンの作成と配置
buttons = [[None, None, None], [None, None, None], [None, None, None]]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(window, text=" ", width=5, height=2, font=(
            "Arial", 24), command=lambda i=i, j=j: game(i, j, buttons[i][j]))
        buttons[i][j].grid(row=i+1, column=j, padx=0, pady=0)

# リセットボタンの作成と配置
reset_button = tk.Button(window, text="リセット", font=(
    "Arial", 14), command=reset_game)
reset_button.grid(row=5, column=0, columnspan=3, pady=10)

# メインループの開始
window.mainloop()
