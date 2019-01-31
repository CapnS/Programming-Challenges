import pygame
from board import Board
import sys

class Game:
    def __init__(self):
        self.board = Board()
    
    def start(self):
        width = 0
        while width < 5 or width > 64:
            try:
                width = int(input("How wide do you want your board? :"))
            except:
                print("Not a valid width")
        height = 0
        while height < 5 or height > 36:
            try:
                height = int(input("How tall do you want your board? :"))
            except:
                print("Not a valid height")
        bombs = 0
        while bombs < 1 or bombs > 100:
            try:
                bombs = int(input("How many mines do you want? :"))
            except:
                print("Not a valid number of bombs")
        self.board.start((width, height, bombs))

    def move(self):
        won = self.board.won()
        if won:
            print("YOU WIN")
            pygame.time.delay(1000)
            sys.exit(0)
        (r,c), right = self.board.get_move()
        if right:
            if self.board.board[r][c] == "f":
                self.board.board[r][c] = "u"
            elif self.board.board[r][c] == "u":
                self.board.board[r][c] = "f"
            elif self.board.board[r][c] == "um":
                self.board.board[r][c] = "fm"
            elif self.board.board[r][c] == "fm":
                self.board.board[r][c] = "um"
        else:
            if self.board.board[r][c] == "um":
                for h in range(self.board.h):
                    for w in range(self.board.w):
                        if self.board.board[h][w] in ("um", "fm"):
                            self.board.board[h][w] = "m"
                self.board.board[r][c] = "lm"
                self.board.draw()
                print("YOU LOSE")
                pygame.time.delay(1000)
                sys.exit(0)
            else:
                mines = self.board.get_neighbors((r,c))
                if mines != "0":
                    self.board.board[r][c] = mines
                else:
                    self.board.open_tiles((r,c))
        self.board.draw()



g = Game()
g.start()
while True:
    g.move()