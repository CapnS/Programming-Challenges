import pygame
from pygame.locals import *
import random
import os
import sys
from collections import deque
import pathlib

class Board:
	def __init__(self):
		os.environ['SDL_VIDEO_CENTERED'] = '1'
		pygame.init()
		pygame.display.init()
		pygame.display.set_caption("Minesweeper")
		dir_path = os.path.dirname(os.path.realpath(__file__))
		self.mine = pygame.image.load(os.path.join(dir_path, os.path.join("images","mine.jpg")))
		self.mine = pygame.transform.scale(self.mine, (30,30))
		self.losingmine = pygame.image.load(os.path.join(dir_path, os.path.join("images","losingmine.jpg")))
		self.losingmine = pygame.transform.scale(self.losingmine, (30,30))
		self.flag = pygame.image.load(os.path.join(dir_path, os.path.join("images","flag.png")))
		self.flag = pygame.transform.scale(self.flag, (30,30))
		self.unknown = pygame.image.load(os.path.join(dir_path, os.path.join("images","unknown.png")))
		self.unknown = pygame.transform.scale(self.unknown, (30,30))
		self.zero = pygame.image.load(os.path.join(dir_path, os.path.join("images","0.png")))
		self.zero = pygame.transform.scale(self.zero, (30,30))
		self.one = pygame.image.load(os.path.join(dir_path, os.path.join("images","1.png")))
		self.one = pygame.transform.scale(self.one, (30,30))
		self.two = pygame.image.load(os.path.join(dir_path, os.path.join("images","2.png")))
		self.two = pygame.transform.scale(self.two, (30,30))
		self.three = pygame.image.load(os.path.join(dir_path,os.path.join("images","3.png")))
		self.three = pygame.transform.scale(self.three, (30,30))
		self.four = pygame.image.load(os.path.join(dir_path, os.path.join("images","4.png")))
		self.four = pygame.transform.scale(self.four, (30,30))
		self.five = pygame.image.load(os.path.join(dir_path, os.path.join("images","5.png")))
		self.five = pygame.transform.scale(self.five, (30,30))
		self.six = pygame.image.load(os.path.join(dir_path, os.path.join("images","6.png")))
		self.six = pygame.transform.scale(self.six, (30,30))
		self.seven = pygame.image.load(os.path.join(dir_path, os.path.join("images","7.png")))
		self.seven = pygame.transform.scale(self.seven, (30,30))
		self.eight = pygame.image.load(os.path.join(dir_path, os.path.join("images","8.png")))
		self.eight = pygame.transform.scale(self.eight, (30,30))
		self.square_size = 30
		self.boardStart_x = 0
		self.boardStart_y = 0
		self.boxes = {
						"m": self.mine,
						"f": self.flag,
						"fm": self.flag,
						"u": self.unknown,
						"um": self.unknown,
						"lm": self.losingmine,
						"0": self.zero,
						"1": self.one,
						"2": self.two,
						"3": self.three,
						"4": self.four,
						"5": self.five,
						"6": self.six,
						"7": self.seven,
						"8": self.eight
					}

	def start(self, size):
		w, h, b = size
		self.w = w
		self.h = h
		self.board = [["u"]*w for _ in range(h)]
		for _ in range(b):
			x = random.randint(0, h-1)
			y = random.randint(0, w-1)
			while self.board[x][y] == 1:
				x = random.randint(0, h-1)
				y = random.randint(0, w-1)
			self.board[x][y] = "um"
		self.screen = pygame.display.set_mode((w*30, h*30))
		for r in range(h):
			for c in range(w):
				(screenX,screenY) = self.screen_coords((r,c))
				self.screen.blit(self.unknown, (screenX, screenY))
		pygame.display.update()

	def draw(self):
		for r in range(self.h):
			for c in range(self.w):
				box = self.board[r][c]
				box = self.boxes[box]
				(screenX,screenY) = self.screen_coords((r,c))
				self.screen.blit(box, (screenX, screenY))
		pygame.display.update()

	def screen_coords(self, square):
		(row,col) = square
		screenX = self.boardStart_x + col*self.square_size
		screenY = self.boardStart_y + row*self.square_size
		return (screenX,screenY)
		
	def chess_coords(self, position):
		(X,Y) = position
		row = (Y-self.boardStart_y) / self.square_size
		col = (X-self.boardStart_x) / self.square_size
		return (row,col)

	def get_move(self):
		while True:
			squareClicked = []
			pygame.event.set_blocked(MOUSEMOTION)
			e = pygame.event.wait()
			if e.type is KEYDOWN:
				if e.key is K_ESCAPE:
					fromSquareChosen = 0
					fromTuple = []
			if e.type is MOUSEBUTTONDOWN:
				(mouseX,mouseY) = pygame.mouse.get_pos()
				squareClicked = self.chess_coords((mouseX,mouseY))
				if squareClicked[0]<0 or squareClicked[0]>self.h or squareClicked[1]<0 or squareClicked[1]>self.w:
					squareClicked = []
				if e.button == 3:
					right = True
				else:
					right = False
			if e.type is QUIT:
				pygame.quit()
				sys.exit(0)
			if squareClicked:
				squareClicked = (int(squareClicked[0]),int(squareClicked[1]))
				return (squareClicked, right)

	def get_neighbors(self, cell):
		r, c = cell
		amount = 0
		if r != 0:
			if c != 0:
				if self.board[r-1][c-1] in ("um", "fm"):
					amount+=1
			if self.board[r-1][c] in ("um", "fm"):
				amount+=1
			if c != self.w-1:
				if self.board[r-1][c+1] in ("um", "fm"):
					amount+=1
		if c != 0:
			if self.board[r][c-1] in ("um", "fm"):
				amount+=1
		if c != self.w-1:
			if self.board[r][c+1] in ("um", "fm"):
				amount+=1
		if r != self.h-1:
			if c!=0:
				if self.board[r+1][c-1] in ("um", "fm"):
					amount+=1
			if self.board[r+1][c] in ("um", "fm"):
				amount+=1
			if c!=self.w-1:
				if self.board[r+1][c+1] in ("um", "fm"):
					amount+=1
		return str(amount)
	
	def open_tiles(self, cell):
		reveal = list()
		reveal.append(cell)
		while reveal:
			r, c = reveal.pop(0)
			if int(self.get_neighbors((r, c))) > 0:
				continue
			neighbors = self.get_surrounding((r, c))
			for k, l in neighbors:
				if self.board[k][l] == "u":
					self.board[k][l] = self.get_neighbors((k,l))
					reveal.append((k, l))

	def get_surrounding(self, cell):
		sur = []
		r, c = cell
		if r > 0:
			sur.append((r-1, c))
			if c > 0:
				sur.append((r-1, c-1))
			if c < self.w-1:
				sur.append((r-1, c+1))
		if c > 0:
			sur.append((r, c-1))
		if c < self.w-1:
			sur.append((r, c+1))
		if r < self.h-1:
			sur.append((r+1, c))
			if c > 0:
				sur.append((r+1, c-1))
			if c < self.w-1:
				sur.append((r+1, c+1))
		return sur
			
	def won(self):
		for r in range(self.h):
			for c in range(self.w):
				if self.board[r][c] in ("um", "u", "f"):
					return False
		return True
	