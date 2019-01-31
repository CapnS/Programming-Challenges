import pygame
from pygame.locals import *
import random
import os
import webcolors
import sys
import time

#setting up the path for loading images
path = os.path.dirname(os.path.realpath(__file__))

#setting os environment variable so that the game is centered on the screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

class Game:
	def __init__(self):
		#doing init for all pygame modules
		pygame.init()
		pygame.display.init()
		pygame.font.init()

		#setting up font for writing the score
		self.f = pygame.font.get_default_font()
		self.font = pygame.font.Font(self.f, 40)
		self.font_x = 241 
		self.font_y = 233

		#loading base image of the game
		self.simon = pygame.image.load(
						os.path.join(path, "images", "simon.png"))
		self.simon = pygame.transform.scale(self.simon, (400,400))

		#loading image to cover up tiles
		self.black = pygame.image.load(
						os.path.join(path, "images", "black.jpg"))
		self.black = pygame.transform.scale(self.black, (200,200))

		#loading start button
		self.start_button = pygame.image.load(
						os.path.join(path, "images", "start.png"))
		self.start_button = pygame.transform.scale(self.start_button, (150,100))

		#setting up the screen
		self.screen = pygame.display.set_mode((500, 500))
		pygame.display.set_caption("Simon")

		#setting up game variables
		self.score = 0
		self.playing = False
		self.pattern = list()
		self.colors = ["red", "green", "yellow", "blue"]

	def draw(self):
		'''Update the screen'''
		#render the score
		score = self.font.render(str(self.score), False, [255, 255, 255], [0, 0, 0])
		#blit the score on the screen
		self.screen.blit(score, (self.font_x, self.font_y))
		#update the screen
		pygame.display.update()

	def start(self):
		'''Start the Game'''
		#blitting the game image centered on the screen
		self.screen.blit(self.simon, (50,50))

		#blitting the start button
		self.screen.blit(self.start_button, (0,0))

		#updating the screen to show everything
		pygame.display.update()

		while True:
			#get clicks
			x, y = self.get_click()
			#user clicked on the button
			if x < 150 and y < 1000:
				#hide the button by blitting black over it
				black = pygame.transform.scale(self.black, (144,88))
				self.screen.blit(black, (0,0))
				self.draw()
				#actually starting the game
				self.playing = True
				self.play()
	
	def play(self):
		'''Playing the actual game'''
		while self.playing:
			#set the pattern
			#self.pattern = list()
			self.pattern.append(random.choice(self.colors))

			#wait so the user can get ready
			time.sleep(.5)
			
			#loop over the patter
			for c in self.pattern:
				#call pygame to get an event so the program doesnt close
				pygame.event.get()
				#set the coordinates to place the black box based on the color
				if c == "green":
					block = (50,50)
				elif c == "red":
					block = (250,50)
				elif c == "yellow":
					block = (50, 250)
				else:
					block = (250,250)
				#blit the black box to the screen and update
				self.screen.blit(self.black, block)
				self.draw()
				#wait .5 seconds so the user can see the change
				time.sleep(.5)
				#blit the game back onto the screen and update
				self.screen.blit(self.simon, (50,50))
				self.draw()
				#wait .25 seconds to start again
				time.sleep(.25)


			#loop to get all inputs
			for i in range(self.score+1):
				#get the player's click
				pos = self.get_click()
				#get RGB of the pixel
				color = self.screen.get_at((pos))
				color = color[0:3]
				#get name of the RGB
				name = self.get_color_name(color)
				if self.pattern[i] == name:
					#player clicked right color so do nothing yet
					pass
				else:
					#player clicked wrong color so they lose
					print("lost")
					sys.exit(0)

			#add one to the score
			self.score+=1

			#changing font size based on score
			if self.score > 9:
				self.font = pygame.font.Font(self.f, 30)
				self.font_x = 237
				self.font_y = 236

			#update the screen
			self.draw()

	def get_click(self):
		'''Get a click from a player'''
		#set clicked to start the loop
		clicked = ()
		while not clicked:
			#block mouse movement for pygame
			pygame.event.set_blocked(MOUSEMOTION)
			#wait for an event from pygame
			e = pygame.event.wait()
			if e.type is MOUSEBUTTONDOWN:
				#get mouse position
				clicked = pygame.mouse.get_pos()
			#to exit the game if player clicks the red X
			if e.type is QUIT:
				sys.exit(0)
			#return the tuple of (x,y) of the mouse click
		return clicked

	def closest_color(self, color):
		'''Get the closest color name from RGB'''
		#setting up dict
		min_colors = {}
		#looping over names of colors
		for key, name in webcolors.css3_hex_to_names.items():
			#get rgb of the colors
			r_c, g_c, b_c = webcolors.hex_to_rgb(key)
			#setting variables to add later
			rd = (r_c - color[0]) ** 2
			gd = (g_c - color[1]) ** 2
			bd = (b_c - color[2]) ** 2
			#setting the value in the dict
			min_colors[(rd + gd + bd)] = name
		#return the name by getting the minimal value
		return min_colors[min(min_colors.keys())]

	def get_color_name(self, color):
		'''Get a color's name based on RGB'''
		try:
			#try getting direct name
			name = webcolors.rgb_to_name(color)
		except ValueError:
			#get the closest name if not possible
			name = self.closest_color(color)
		#get basic name of the color
		if name in ("limegreen", "palegreen", "lightgreen", 
					"lightgrey", "gainsboro", "powderblue",
					"silver", "mediumseagreen"):
			color = "green"
		elif name in ("chocolate", "burlywood", "orangered", 
					"firebrick", "lightcoral", "darksalmon", 
					"indianred", "lightpink", "pink", "mistyrose",
					"antiquewhite", "bisque", "tan", "salmon"):
			color = "red"
		elif name in ("yellow", "darkgoldenrod", "goldenrod","gold"):
			color = "yellow"
		elif name in ("blue", "mediumblue"):
			color = "blue"
		else:
			color = name
		#return the name of the color
		return color

Game().start()