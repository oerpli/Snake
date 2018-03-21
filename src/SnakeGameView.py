from RectangleDrawer import *
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
		
		self.canvas = tk.Canvas(self.window, bg="#666", height=GameBoard.SIZE_Y*SnakeGameView.SNAKE_WIDTH, width=GameBoard.SIZE_X*SnakeGameView.SNAKE_WIDTH)
		self.gameScoreLabel = tk.Label(self.window)
		self.gameInfoLabel = tk.Label(self.window)
		self.numPlayers = 4
		self.shouldStartNewGame = False
		self.startGame()
		self.initKeyDict()
		self.window.bind_all("<Key>", self.keyPressed)
		# self.window.bind_all("<KeyRelease>", self.keyReleased)
		self.fnCall = self.window.after(SnakeGameView.REDRAW_DELAY, self.animate) 
		self.window.mainloop()

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
		if self.shouldStartNewGame:
			self.shouldStartNewGame = False
			self.startGame()
			return
		(self.snakes, self.food) = self.Game.Step()

		for snake in self.snakes:
			if not snake.IsAlive():
				self.handleGameOver()
				return

		self.canvas.delete("all")
		for snake in self.snakes:
			snake.Draw()
		self.food.Draw()
		self.canvas.pack()

		self.updateGameInfo()
		self.window.after(SnakeGameView.GAME_DELAY, self.gameLoop)

	def handleGameOver(self):
		self.updateGameInfo(gameOver = True)

		SnakeGameView.GAME_OVER = True

	def updateGameInfo(self, score = 0, gameOver = False):
		self.window.title("Snake - {} {}".format(self.numPlayers, 'player' if self.numPlayers == 1 else 'players'))
		self.gameScoreLabel.config(text = self.getScoreString())

		if gameOver:
			self.gameInfoLabel.config(text="Game Over! - press space to restart", fg="red")
		else:
			self.gameInfoLabel.config(text="Game running", fg="black")
			
		self.gameInfoLabel.pack()
		self.gameScoreLabel.pack()

	def getScoreString(self):
		i = 65
		scoresStrings = []
		for snake in self.snakes:
			scoresStrings.append("Snake {}: {}".format(chr(i), snake.Score))
			i += 1

		return "; ".join(scoresStrings)

	def startGame(self):
		self.score = 0
		self.canvas.delete("all")
		SnakeGameView.GAME_OVER = False
		self.Game = GameBoard(self.numPlayers)
		self.Game.Food.InitDrawer(RectangleDrawer(self.canvas,self.SNAKE_WIDTH))
		self.snakes = self.Game.GetSnakes()
		for snake in self.snakes:
			drawer = RectangleDrawer(self.canvas,self.SNAKE_WIDTH)
			snake.InitDrawer(drawer)
		# self.addPoint((3,2), 'RIGHT')
		self.currentRect = None

		self.window.after(SnakeGameView.GAME_DELAY, self.gameLoop) 

	def keyPressed(self, event):
		if SnakeGameView.GAME_OVER and event.keysym == 'space':
			self.startGame()
			return
		if event.keysym == '1':
			self.numPlayers = 1
			self.shouldStartNewGame = True
			return
		if event.keysym == '2':
			self.numPlayers = 2
			self.shouldStartNewGame = True
			return
		if event.keysym == '3':
			self.numPlayers = 3
			self.shouldStartNewGame = True
			return
		if event.keysym == '4':
			self.numPlayers = 4
			self.shouldStartNewGame = True
			return
		
		key = self.KeyDict.get(event.keysym, None)
		if key is not None:
			(snake,dir) = key
			self.snakes[snake].NewDirection = dir

	def initKeyDict(self):
		P0 = ['Up','Down','Left','Right']
		P1 = list('wsad')
		P2 = list('ikjl')
		P3 = list('tgfh')
		p0d = self.playerKeyDict(P0,0)
		p1d = self.playerKeyDict(P1,1)
		p2d = self.playerKeyDict(P2,2)
		p3d = self.playerKeyDict(P3,3)
		self.KeyDict = {**p0d, **p1d, **p2d, **p3d}

		
	def playerKeyDict(self, keys, playerNumber):
		# keys should be list of key events in the order:
		# UP DOWN LEFT RIGHT (WSAD)
		playerdict = dict()
		for (key,dir) in zip(keys,[Direction.DOWN,Direction.UP,Direction.LEFT,Direction.RIGHT]):
			playerdict[key] = (playerNumber,dir)
		return playerdict

	# def keyReleased(self, event):
		# self.moveDirX = 0
		# self.moveDirY = 0

a = SnakeGameView()
