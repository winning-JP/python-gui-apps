import tkinter as tk
from tkinter import messagebox
from functools import partial
import random
import sys
import pygame


screenHeight = 390
screenWidth = 390


def play_victory_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("victory_sound.mp3")  # ここに再生したい音声ファイルのパスを指定
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()


def play_lose_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("lose_sound.mp3")  # ここに再生したい音声ファイルのパスを指定
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()


def play_dorow_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("dorow_sound.mp3")  # ここに再生したい音声ファイルのパスを指定
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.mainframe = tk.Frame(self.master)
        self.mainframe.pack()

        self.frame1 = tk.Frame(self.master)
        self.frame1.grid(row=0, column=0, in_=self.mainframe, pady=50)

        self.cells = [[tk.StringVar() for i in range(3)] for j in range(3)]

        self.createButtonsWithGrid(cellSize=9, gridSize=3, fontSize=10)

    def createButtonsWithGrid(self, cellSize, gridSize: int, fontSize=0, cellSpace=0):

        for i in range(0, gridSize):
            for j in range(0, gridSize):
                button = tk.Button(
                    self.frame1,
                    relief="groove",
                    width=cellSize,
                    height=int(cellSize/2),
                    # text=text,
                    textvariable=self.cells[i][j],
                    font=("System", fontSize),
                    command=partial(self.clicked, (i, j))
                )
                button.grid(column=j, row=i, padx=cellSpace, pady=cellSpace)

    def clicked(self, p):
        if (self.checkCell(p, "x")
                or self.checkCell(p, "o")):
            pass
        else:
            self.changeCell(p, "o")
            if self.judgeGame(p, "o"):
                play_victory_sound()
                ans = messagebox.askyesno("勝利", "プレイヤーの勝利です。\nもう一度プレイしますか?")
                if ans:
                    self.resetGame()
                else:
                    sys.exit()
            else:
                enemyPos = self.setEnemy()

                if enemyPos[0] < 0:
                    play_dorow_sound()
                    ans = messagebox.askyesno("引き分け", "引き分けました。\nもう一度プレイしますか?")
                    if ans:
                        self.resetGame()
                    else:
                        sys.exit()

                if self.judgeGame(enemyPos, "x"):
                    play_lose_sound()
                    ans = messagebox.askyesno(
                        "敗北", "あなたは敗北しました。\nもう一度プレイしますか?")
                    if ans:
                        self.resetGame()
                    else:
                        sys.exit()

    def changeCell(self, p, msg):
        print(p)
        self.cells[p[0]][p[1]].set(msg)

    def setEnemy(self):

        if self.checkWholeBoard():
            return (-1, -1)

        i = random.randint(0, len(self.cells)-1)
        j = random.randint(0, len(self.cells)-1)
        while (self.checkCell((i, j), "o")
               or self.checkCell((i, j), "x")):
            i = random.randint(0, len(self.cells)-1)
            j = random.randint(0, len(self.cells)-1)
        self.changeCell((i, j), "x")
        return (i, j)

    def judgeGame(self, p: tuple, c):
        maxIndex = len(self.cells)-1

        if p[0] == maxIndex:
            if p[1] == maxIndex:
                if (self.checkCell((p[0], p[1]-2), c)
                        and self.checkCell((p[0], p[1]-1), c)):
                    return True
                elif (self.checkCell((p[0]-2, p[1]), c)
                      and self.checkCell((p[0]-1, p[1]), c)):
                    return True
                elif (self.checkCell((p[0]-2, p[1]-2), c)
                      and self.checkCell((p[0]-1, p[1]-1), c)):
                    return True
            elif p[1] == 0:
                if (self.checkCell((p[0]-2, p[1]), c)
                        and self.checkCell((p[0]-1, p[1]), c)):
                    return True
                elif (self.checkCell((p[0], p[1]+2), c)
                      and self.checkCell((p[0], p[1]+1), c)):
                    return True
                elif (self.checkCell((p[0]-2, p[1]+2), c)
                      and self.checkCell((p[0]-1, p[1]+1), c)):
                    return True
            else:
                if (self.checkCell((p[0], p[1]-1), c)
                        and self.checkCell((p[0], p[1]+1), c)):
                    return True
                elif (self.checkCell((p[0]-1, p[1]), c)
                      and self.checkCell((p[0]-2, p[1]), c)):
                    return True
                return False

        elif p[0] == 0:
            if p[1] == maxIndex:
                if (self.checkCell((p[0], p[1]-2), c)
                        and self.checkCell((p[0], p[1]-1), c)):
                    return True
                elif (self.checkCell((p[0]+2, p[1]), c)
                      and self.checkCell((p[0]+1, p[1]), c)):
                    return True
                elif (self.checkCell((p[0]+2, p[1]-2), c)
                      and self.checkCell((p[0]+1, p[1]-1), c)):
                    return True
            elif p[1] == 0:
                if (self.checkCell((p[0]+2, p[1]), c)
                        and self.checkCell((p[0]+1, p[1]), c)):
                    return True
                elif (self.checkCell((p[0], p[1]+2), c)
                      and self.checkCell((p[0], p[1]+1), c)):
                    return True
                elif (self.checkCell((p[0]+2, p[1]+2), c)
                      and self.checkCell((p[0]+1, p[1]+1), c)):
                    return True
            else:
                if (self.checkCell((p[0], p[1]-1), c)
                        and self.checkCell((p[0], p[1]+1), c)):
                    return True
                elif (self.checkCell((p[0]+1, p[1]), c)
                      and self.checkCell((p[0]+2, p[1]), c)):
                    return True
                return False

        else:
            if p[1] == 0:
                if (self.checkCell((p[0]-1, p[1]), c)
                        and self.checkCell((p[0]+1, p[1]), c)):
                    return True
                elif (self.checkCell((p[0], p[1]+1), c)
                      and self.checkCell((p[0], p[1]+2), c)):
                    return True
            elif p[1] == maxIndex:
                if (self.checkCell((p[0]-1, p[1]), c)
                        and self.checkCell((p[0]+1, p[1]), c)):
                    return True
                elif (self.checkCell((p[0], p[1]-1), c)
                      and self.checkCell((p[0], p[1]-2), c)):
                    return True
            else:
                if (self.checkCell((p[0]-1, p[1]), c)
                        and self.checkCell((p[0]+1, p[1]), c)):
                    return True
                elif (self.checkCell((p[0], p[1]+1), c)
                      and self.checkCell((p[0], p[1]+1), c)):
                    return True
                if (self.checkCell((p[0]-1, p[1]-1), c)
                        and self.checkCell((p[0]+1, p[1]+1), c)):
                    return True
                elif (self.checkCell((p[0]+1, p[1]-1), c)
                      and self.checkCell((p[0]-1, p[1]+1), c)):
                    return True
                return False

    def checkCell(self, p, c):
        return self.cells[p[0]][p[1]].get() == c

    def checkWholeBoard(self):
        for i in self.cells:
            for j in i:
                if (j.get() == ""):
                    return False
        return True

    def resetGame(self):
        for i in self.cells:
            for j in i:
                j.set("")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("○×ゲーム")

    # Screen size
    root.geometry(str(screenWidth)+"x"+str(screenHeight))

    app = Application(master=root)

    root.mainloop()
