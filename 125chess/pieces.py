import pygame

square_size = 50

def IsClearPath(board,fromTuple,toTuple):
		r = fromTuple[0]
		c = fromTuple[1]
		tr = toTuple[0]
		tc = toTuple[1]
		if abs(r - tr) <= 1 and abs(c - tc) <= 1:
			return True
		else:
			if tr > r and tc == c:
				newTuple = (r+1,c)
			elif tr < r and tc == c:
				newTuple = (r-1,c)
			elif tr == r and tc > c:
				newTuple = (r,c+1)
			elif tr == r and tc < c:
				newTuple = (r,c-1)
			elif tr > r and tc > c:
				newTuple = (r+1,c+1)
			elif tr > r and tc < c:
				newTuple = (r+1,c-1)
			elif tr < r and tc > c:
				newTuple = (r-1,c+1)
			elif tr < r and tc < c:
				newTuple = (r-1,c-1)
		if board[newTuple[0]][newTuple[1]] != 'e':
			return False
		else:
			return IsClearPath(board,newTuple,toTuple)

class Pawn:
	def __init__(self, color):
		self.color = color
		self.image = pygame.image.load("C:/Users/zacha/OneDrive/Documents/Python/Programming Challenges/125chess/images/"+color+"_pawn.png") 
		self.image = pygame.transform.scale(self.image, (square_size,square_size))

	def is_valid(self, board, fromTuple, toTuple, enemy):
		r, c = fromTuple
		tr, tc = toTuple
		if r in (1,6):
			if enemy == "b":
				if tr - r in (-1, -2) and tc - c == 0 and board[tr][tc] == "e" and board[tr + 1][tc] in ("e", "wP"):
					return True
				if tr - r == -1 and tc - c in (1, -1) and enemy in board[tr][tc]:
					return True
			else:
				if tr - r in (1, 2) and tc - c == 0 and board[tr][tc] == "e" and board[tr - 1][tc] in ("e", "bP"):
					return True
				if tr - r == 1 and tc - c in (1, -1) and enemy in board[tr][tc]:
					return True
		else:
			if enemy == "b":
				if tr - r == -1 and tc - c == 0 and board[tr][tc] == "e":
					return True
				if tr - r == -1 and tc - c in (1, -1) and enemy in board[tr][tc]:
					return True
			else:
				if tr - r == 1 and tc - c == 0 and board[tr][tc] == "e":
					return True
				if tr - r == 1 and tc - c in (1, -1) and enemy in board[tr][tc]:
					return True

class Rook:
	def __init__(self, color):
		self.color = color
		self.image = pygame.image.load("C:/Users/zacha/OneDrive/Documents/Python/Programming Challenges/125chess/images/"+color+"_rook.png") 
		self.image = pygame.transform.scale(self.image, (square_size,square_size))

	def is_valid(self, board, fromTuple, toTuple, enemy):
		r, c = fromTuple
		tr, tc = toTuple
		if (tr == r or tc == c) and (board[tr][tc] == "e" or enemy in board[tr][tc]):
			if IsClearPath(board,fromTuple,toTuple):
				return True

class Knight:
	def __init__(self, color):
		self.color = color
		self.image = pygame.image.load("C:/Users/zacha/OneDrive/Documents/Python/Programming Challenges/125chess/images/"+color+"_knight.png") 
		self.image = pygame.transform.scale(self.image, (square_size,square_size))

	def is_valid(self, board, fromTuple, toTuple, enemy):
		r, c = fromTuple
		tr, tc = toTuple
		if tr - r in (2,-2) and tc - c in (1,-1) and (board[tr][tc] == "e" or enemy in board[tr][tc]):
			return True
		if tc - c in (2, -2) and tr - r in (1, -1) and (board[tr][tc] == "e" or enemy in board[tr][tc]):
			return True

class Bishop:
	def __init__(self, color):
		self.color = color
		self.image = pygame.image.load("C:/Users/zacha/OneDrive/Documents/Python/Programming Challenges/125chess/images/"+color+"_bishop.png")
		self.image = pygame.transform.scale(self.image, (square_size,square_size))

	def is_valid(self, board, fromTuple, toTuple, enemy):
		r, c = fromTuple
		tr, tc = toTuple
		if (abs(tr - r) == abs(tc - c)) and (board[tr][tc] == 'e' or enemy in board[tr][tc]):
			if IsClearPath(board,fromTuple,toTuple):
				return True

class Queen:
	def __init__(self, color):
		self.color = color
		self.image = pygame.image.load("C:/Users/zacha/OneDrive/Documents/Python/Programming Challenges/125chess/images/"+color+"_queen.png")
		self.image = pygame.transform.scale(self.image, (square_size,square_size))

	def is_valid(self, board, fromTuple, toTuple, enemy):
		tr, tc = toTuple
		if (board[tr][tc] == "e" or enemy in board[tr][tc]):
			if IsClearPath(board,fromTuple,toTuple):
				return True

class King:
	def __init__(self, color):
		self.color = color
		self.image = pygame.image.load("C:/Users/zacha/OneDrive/Documents/Python/Programming Challenges/125chess/images/"+color+"_king.png")
		self.image = pygame.transform.scale(self.image, (square_size,square_size))

	
	def is_valid(self, board, fromTuple, toTuple, enemy):
		tr, tc = toTuple
		r, c = fromTuple
		if tr - r in (-1,0,1) and tc - c in (-1,0,1) and (board[tr][tc] == "e" or enemy in board[tr][tc]):
			return True
	