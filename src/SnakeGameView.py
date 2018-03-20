import tkinter as tk
from collections import deque
from Direction import *
from GameBoard import *
from Snake import *
import time

class SnakeGameView:
	SNAKE_WIDTH = 14
	REDRAW_DELAY = 1000//60# 60FPS
	GAME_DELAY = 125
	GAME_OVER = False

	def __init__(self):
		self.window = tk.Tk()
		
		self.canvas = tk.Canvas(self.window, bg="grey", height=GameBoard.SIZE_Y*SnakeGameView.SNAKE_WIDTH, width=GameBoard.SIZE_X*SnakeGameView.SNAKE_WIDTH)
		self.gameInfoLabel = tk.Label(self.window)

		self.startGame()

		self.window.bind_all("<Key>", self.keyPressed)
		# self.window.bind_all("<KeyRelease>", self.keyReleased)
		self.window.after(SnakeGameView.REDRAW_DELAY, self.animate) 
		self.window.mainloop()

	def drawSnakes(self, snakes):
		for snake in snakes:
			for rect in snake.GetCoordinates():
				x = rect[0] * SnakeGameView.SNAKE_WIDTH
				y = rect[1] * SnakeGameView.SNAKE_WIDTH
				self.canvas.create_rectangle(x, y, x + SnakeGameView.SNAKE_WIDTH, y + SnakeGameView.SNAKE_WIDTH, fill="black")

	def drawFood(self, rect):
		x = rect[0] * SnakeGameView.SNAKE_WIDTH
		y = rect[1] * SnakeGameView.SNAKE_WIDTH
		self.canvas.create_rectangle(x, y, x + SnakeGameView.SNAKE_WIDTH, y + SnakeGameView.SNAKE_WIDTH, fill="red")

	def addPoint(self, point, drawingDirection):
		# adds a new point and prepares it to be rendered in the animate function
		x = point[0] * SnakeGameView.SNAKE_WIDTH
		y = point[1] * SnakeGameView.SNAKE_WIDTH

		self.currentRect = self.canvas.create_rectangle(x, y, x + SnakeGameView.SNAKE_WIDTH, y + SnakeGameView.SNAKE_WIDTH, fill="black")

		self.change = SnakeGameView.SNAKE_WIDTH *1
		self.startTime = int(round(time.time()*1000)) 
		self.startValue = x
		self.easingDuration = 1000

	def animate(self):
		if (self.currentRect is not None): 
			currentTime = int(round(time.time()*1000))
			currentDuration = currentTime - self.startTime

			animationProgress = currentDuration / self.easingDuration

			coords = self.canvas.coords(self.currentRect)
			coords[2] = self.startValue + self.change * animationProgress

			self.canvas.coords(self.currentRect, coords)

			if (animationProgress >= 1.0):
				self.currentRect = None

		self.window.after(SnakeGameView.REDRAW_DELAY, self.animate)

	def gameLoop(self):
		(self.snakes, self.food) = self.Game.Step()

		self.canvas.delete("all")
		self.drawSnakes(self.snakes)
		self.drawFood(self.food)
		self.canvas.pack()

		# for snake in self.snakes:
		# 	if not snake.IsAlive():
		# 		self.handleGameOver()
		# 		return

		# self.updateGameInfo(score)
		self.window.after(SnakeGameView.GAME_DELAY, self.gameLoop)

	def handleGameOver(self):
		# self.updateGameInfo(self.score, gameOver = True)

		SnakeGameView.GAME_OVER = True

	def updateGameInfo(self, score = 0, gameOver = False):
		if not gameOver:
			self.gameInfoLabel.config(text = "Current Score: " + str(score), fg="black")
		else:
			self.gameInfoLabel.config(text = "Game Over - Final Score: " + str(score) + " - Press Space to Restart", fg="red")
			
		self.gameInfoLabel.pack()

	def startGame(self):
		self.score = 0
		self.canvas.delete("all")
		SnakeGameView.GAME_OVER = False

		self.Game = GameBoard()

		# self.addPoint((3,2), 'RIGHT')
		self.currentRect = None

		self.window.after(SnakeGameView.GAME_DELAY, self.gameLoop) 

	def keyPressed(self, event):
		print("key {} pressed".format(event.keysym))
		
		if SnakeGameView.GAME_OVER and event.keysym == 'space':
			self.startGame()
			return

		if (event.keysym == 'Right'):
			self.snakes[0].NewDirection = Direction.RIGHT
		elif (event.keysym == 'Left'):
			self.snakes[0].NewDirection = Direction.LEFT
		elif (event.keysym == 'Down'):
			self.snakes[0].NewDirection = Direction.UP
		elif event.keysym == 'Up':
			self.snakes[0].NewDirection = Direction.DOWN
		elif event.keysym == 'd':
			self.snakes[1].NewDirection = Direction.RIGHT
		elif event.keysym == 'a':
			self.snakes[1].NewDirection = Direction.LEFT
		elif event.keysym == 's':
			self.snakes[1].NewDirection = Direction.UP
		elif event.keysym == 'w':
			self.snakes[1].NewDirection = Direction.DOWN

	# def keyReleased(self, event):
		# self.moveDirX = 0
		# self.moveDirY = 0

a = SnakeGameView()
