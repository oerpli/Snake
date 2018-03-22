from RectangleDrawer import *
from SingleColorGenerator import *
from BlinkingColorGenerator import *
from GameOverState import *
from GameRunningState import *
from ShouldStartNewGameState import *
import tkinter as tk
from collections import deque
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

		self.gameOverState = GameOverState(self)
		self.gameRunningState = GameRunningState(self)
		self.shouldStartNewGameState = ShouldStartNewGameState(self)
		self.currentState = self.gameRunningState
		
		self.initView()
		self.startGame()

		self.window.bind_all("<Key>", self.keyPressed)

		self.window.after(SnakeGameView.GAME_DELAY, self.gameLoop) 
		self.window.mainloop()

	def initView(self):
		self.canvas = tk.Canvas(self.window, bg="#666", height=GameBoard.SIZE_Y*SnakeGameView.SNAKE_WIDTH, width=GameBoard.SIZE_X*SnakeGameView.SNAKE_WIDTH)
		self.gameScoreLabel = tk.Label(self.window)
		self.gameInfoLabel = tk.Label(self.window)
		self.numPlayers = 2
		self.foodDrawer = RectangleDrawer(self.canvas, self.SNAKE_WIDTH, BlinkingColorGenerator())
		self.food = None

	def gameLoop(self):
		self.currentState.render()
		self.window.after(SnakeGameView.GAME_DELAY, self.gameLoop)

	def handleGameOver(self):
		self.currentState = self.gameOverState

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

		self.Game = GameBoard(self.numPlayers)
		self.Game.Food.InitDrawer(self.foodDrawer)
		self.snakes = self.Game.GetSnakes()
		colors = ["#ABFF19", "#E8C217", "#FF9526", "#E82C17", "#F968FF"]
		for (i, snake) in enumerate(self.snakes):
			drawer = RectangleDrawer(self.canvas,self.SNAKE_WIDTH,SingleColorGenerator(colors[i]))
			snake.InitDrawer(drawer)

		self.currentRect = None

		self.currentState = self.gameRunningState

	def keyPressed(self, event):
		self.currentState.keyPressed(event)
		
a = SnakeGameView()
