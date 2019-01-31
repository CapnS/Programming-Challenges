import pygame
from pygame.locals import *
from pieces import *
import sys
import copy

class Board:
	def __init__(self):
		pygame.init()
		pygame.font.init()
		self.screen = pygame.display.set_mode((500, 500))
		pygame.display.set_caption("Chess")
		f = pygame.font.get_default_font()
		self.font = pygame.font.Font(f, 20)
		self.boardStart_x = 50
		self.boardStart_y = 50
		self.square_size = 50
		self.white_square = pygame.image.load("C:/Users/zacha/OneDrive/Documents/Python/Programming Challenges/125chess/images/white_square.png").convert()
		self.brown_square = pygame.image.load("C:/Users/zacha/OneDrive/Documents/Python/Programming Challenges/125chess/images/brown_square.png").convert()
		self.has_moved = {
							(0,0): False,
							(0,4): False,
							(0,7): False,
							(7,0): False,
							(7,4): False,
							(7,7): False
						}

		self.board = [
						['bR','bT','bB','bQ','bK','bB','bT','bR'],
						['bP','bP','bP','bP','bP','bP','bP','bP'],
						['e','e','e','e','e','e','e','e'],
						['e','e','e','e','e','e','e','e'],
						['e','e','e','e','e','e','e','e'],
						['e','e','e','e','e','e','e','e'],
						['wP','wP','wP','wP','wP','wP','wP','wP'],
						['wR','wT','wB','wQ','wK','wB','wT','wR']
					]			
		self.pieces = {
						"bR": Rook("black"),
						"bT": Knight("black"),
						"bB": Bishop("black"),
						"bQ": Queen("black"),
						"bK": King("black"),
						"bP": Pawn("black"),
						"wR": Rook("white"),
						"wT": Knight("white"),
						"wB": Bishop("white"),
						"wQ": Queen("white"),
						"wK": King("white"),
						"wP": Pawn("white")
					}

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
	
	def draw(self):
		current_square = 0
		for r in range(8):
			for c in range(8):
				(screenX,screenY) = self.screen_coords((r,c))
				if current_square:
					self.screen.blit(self.brown_square,(screenX,screenY))
					current_square = (current_square+1)%2
				else:
					self.screen.blit(self.white_square,(screenX,screenY))
					current_square = (current_square+1)%2
			current_square = (current_square+1)%2

		for r in range(8):
			for c in range(8):
				(screenX,screenY) = self.screen_coords((r,c))
				if not self.board[r][c] == "e":
					self.screen.blit(self.pieces[self.board[r][c]].image,(screenX,screenY))
		
		pygame.display.update()

	def get_move(self,currentColor):
		fromSquareChosen = 0
		toSquareChosen = 0
		while not fromSquareChosen or not toSquareChosen:
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
				if squareClicked[0]<0 or squareClicked[0]>8 or squareClicked[1]<0 or squareClicked[1]>8:
					squareClicked = [] 
			if e.type is QUIT:
				pygame.quit()
				sys.exit(0)
			if squareClicked:
				squareClicked = (int(squareClicked[0]),int(squareClicked[1]))
				p = currentColor[0]
				r,c = squareClicked
				if not fromSquareChosen and not toSquareChosen:
					if p in self.board[r][c]:
						fromSquareChosen = 1
						fromTuple = squareClicked
					else:
						continue
				elif fromSquareChosen and not toSquareChosen:
					enemy = "b" if p == "w" else "w"
					fr, fc = fromTuple
					if (r,c) == fromTuple:
						fromSquareChosen = 0
						continue
					if self.pieces[self.board[fr][fc]].is_valid(self.board, fromTuple, (r,c), enemy):
						board = copy.copy(self.board)
						board[r][c] = board[fr][fc]
						board[fr][fc] = "e"
						if not self.IsCheck(board, p):
							board[fr][fc] = board[r][c]
							board[r][c] = "e"
							toSquareChosen = 1
							toTuple = squareClicked
						else:
							board[fr][fc] = board[r][c]
							board[r][c] = "e"
							fromSquareChosen = 0
							print("You cant do that, it puts you in check")
					elif self.IsCastle(fromTuple, squareClicked, p):
						return(fromTuple, squareClicked, True)
					else:
						fromSquareChosen = 0
		if fromTuple in	((0,4),(7,4),(0,0),(0,7),(7,0),(7,7)):
			self.has_moved[fromTuple] = True
		return (fromTuple,toTuple, None)
	
	def get_king(self, board, color):
		for r in range(8):
			for c in range(8):
				if board[r][c] == color+"K":
					return (r,c)
		return (0,4)

	def IsCheck(self, board, color):
		enemy = "b" if color == "w" else "w"
		king = self.get_king(board, color)
		for r in range(8):
			for c in range(8):
				if enemy in board[r][c]:
					if self.pieces[board[r][c]].is_valid(board, (r,c), king, color):
						return True
	
	def IsCheckMate(self, color):
		if not self.IsCheck(self.board, color):
			return False
		for r in range(8):
			for c in range(8):
				for tr in range(8):
					for tc in range(8):
						f = (r, c)
						to = (tr, tc)
						if color in self.board[r][c]:
							if self.board[tr][tc] == "e":
								if self.pieces[self.board[r][c]].is_valid(self.board, f, to, color):
									board = copy.copy(self.board)
									board[tr][tc] = board[r][c]
									board[r][c] = "e"
									if not self.IsCheck(board, color):
										board[r][c] = board[tr][tc]
										board[tr][tc] = "e"
										return False
									else:
										board[r][c] = board[tr][tc]
										board[tr][tc] = "e"
		return True

	def IsStaleMate(self, color):
		for r in range(8):
			for c in range(8):
				for tr in range(8):
					for tc in range(8):
						f = (r, c)
						to = (tr, tc)
						if not (self.board[r][c] == "e") or (color in self.board[r][c]): 
							if self.IsCheck(self.board, color):
								return False
							elif self.pieces[self.board[r][c]].is_valid(self.board, f, to, color):
								return False
		return True

	def IsCastle(self, fromTuple, toTuple, p):
		if not fromTuple in ((0,4),(7,4)) or not toTuple in ((0,2),(0,6),(7,2),(7,6)):
			return False
		if self.has_moved[fromTuple]:
			return False
		if not IsClearPath(self.board, fromTuple, toTuple):
			return False
		board = copy.copy(self.board)
		if toTuple == (0,2):
			if self.has_moved[(0,0)]:
				return False
			board[0][0] = "e"
			board[0][2] = "bK"
			board[0][3] = "bR"
			board[0][4] = "e"
			if self.IsCheck(board, p):
				return False			
		elif toTuple == (0,6):
			if self.has_moved[(0,7)]:
				return False
			board[0][7] = "e"
			board[0][6] = "bK"
			board[0][5] = "bR"
			board[0][4] = "e"
			if self.IsCheck(board, p):
				return False
		elif toTuple == (7,2):
			if self.has_moved[(7,0)]:
				return False
			board[7][0] = "e"
			board[7][2] = "wK"
			board[7][3] = "wR"
			board[7][4] = "e"
			if self.IsCheck(board, p):
				return False
		elif toTuple == (7,6):
			if self.has_moved[(7,7)]:
				return False
			board[7][7] = "e"
			board[7][6] = "wK"
			board[7][5] = "wR"
			board[7][4] = "e"
			if self.IsCheck(board, p):
				return False
		return True
