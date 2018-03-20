import tkinter as tk
from collections import deque
from Direction import *
from GameBoard import *
from Snake import *
import time

class SnakeGameView:
	SNAKE_WIDTH = 10
	REDRAW_DELAY = 1000//60# 60FPS
	GAME_DELAY = 125
	GAME_OVER = False

	def __init__(self):
		self.window = tk.Tk()
		self.canvas = tk.Canvas(self.window, bg="grey", height=GameBoard.SIZE_Y*SnakeGameView.SNAKE_WIDTH, width=GameBoard.SIZE_X*SnakeGameView.SNAKE_WIDTH)
		self.labels = []

		self.startGame()

		self.window.bind_all("<Key>", self.keyPressed)
		# self.window.bind_all("<KeyRelease>", self.keyReleased)
		self.window.after(SnakeGameView.REDRAW_DELAY, self.animate) 
		self.window.mainloop()

	def drawSnake(self, points):
		for rect in points:
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
		(oldEnd, newFront, doesLive, newFood) = self.Game.Step(self.Direction)

		if not doesLive:
			self.handleGameOver()
		else:
			self.canvas.delete("all")
			self.drawSnake(self.Game.Snake.GetCoordinates())
			self.drawFood(self.Game.Food)
			self.window.after(SnakeGameView.GAME_DELAY, self.gameLoop)

	def handleGameOver(self):
		self.labels.append(tk.Label(self.window, text="Game Over"))
		self.labels.append(tk.Label(self.window, text="Press space to restart"))

		for label in self.labels:
			label.pack()

		SnakeGameView.GAME_OVER = True

	def startGame(self):
		self.canvas.delete("all")
		SnakeGameView.GAME_OVER = False

		for label in self.labels:
			label.destroy()
		
		self.labels.clear()

		self.Game = GameBoard()
		self.drawSnake(self.Game.Snake.GetCoordinates())
		self.canvas.pack()

		self.Direction = self.Game.Snake.Direction
		# self.addPoint((3,2), 'RIGHT')
		self.currentRect = None

		self.window.after(SnakeGameView.GAME_DELAY, self.gameLoop) 

	def keyPressed(self, event):
		if SnakeGameView.GAME_OVER and event.keysym == 'space':
			self.startGame()
			return

		if (event.keysym == 'Right'):
			self.Direction = Direction.RIGHT
		elif (event.keysym == 'Left'):
			self.Direction = Direction.LEFT
		elif (event.keysym == 'Down'):
			self.Direction = Direction.UP
		elif event.keysym == 'Up':
			self.Direction = Direction.DOWN
			
	# def keyReleased(self, event):
		# self.moveDirX = 0
		# self.moveDirY = 0

a = SnakeGameView()
