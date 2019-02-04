import pygame
from pygame.locals import Color
from board import Board
import sys
import os

class Game:
    def __init__(self):
        self.board = Board()
        self.player = "white"
        text = self.board.font.render(self.player.capitalize()+"'s Turn", False, [255, 255, 255])
        self.board.screen.fill(Color("black"), (190, 460, 300, 600))
        self.board.screen.blit(text, (190, 460)) 
        self.board.draw()

    def move(self):
        if self.board.IsCheckMate(self.player[0]):
            winner = "white" if self.player == "black" else "black"
            dir_path = os.path.dirname(os.path.realpath(__file__))
            checkmate = pygame.image.load(os.path.join(dir_path, os.path.join("images","checkmate_"+winner+".jpg")))
            checkmate = pygame.transform.scale(checkmate, (200,200))
            text = self.board.font.render("Checkmate, "+ winner.capitalize() + " Wins!", False, [255, 255, 255], [0, 0, 0])
            self.board.screen.blit(checkmate, (150,150))
            self.board.screen.blit(text, (130,125))
            pygame.display.update()
            pygame.time.delay(10000)
            sys.exit(0)
        if self.board.IsCheck(self.board.board,self.player[0]):
            print(self.player+ " is in check")
        if self.board.IsStaleMate(self.player[0]):
            dir_path = os.path.dirname(os.path.realpath(__file__))
            stalemate = pygame.image.load(os.path.join(dir_path, os.path.join("images","stalemate.jpg")))
            stalemate = pygame.transform.scale(stalemate, (200,200))
            self.board.screen.blit(stalemate, (150,150))
            pygame.display.update()
            pygame.time.delay(10000)
            sys.exit(0)
        (r,c),(tr,tc), castle = self.board.get_move(self.player)
        if castle:
            pass
        else:
            piece = self.board.board[r][c]
            if piece in("wP", "bP") and tr in (0,7):
                piece = piece[0] + "Q"
            self.board.board[r][c] = "e"
            self.board.board[tr][tc] = piece
        self.player = "white" if self.player == "black" else "black"
        text = self.board.font.render(self.player.capitalize()+"'s Turn", False, [255, 255, 255])
        self.board.screen.fill(Color("black"), (190, 460, 300, 600))
        self.board.screen.blit(text, (190, 460))  
        self.board.draw()    
        
g = Game()
while True:
    g.move()
