from GameOverState import *
from GameRunningState import *
import tkinter as tk
from collections import deque
import time

class SnakeGameView:
	SNAKE_WIDTH = 14
	GAME_LOOP_INTERVAL = 125

	def __init__(self):
		self.window = tk.Tk()
		self.canvas = None

		self.initView()

		self.gameOverState = GameOverState(self)
		self.gameRunningState = GameRunningState(self, SnakeGameView.SNAKE_WIDTH, SnakeGameView.GAME_LOOP_INTERVAL)
		self.currentState = self.gameRunningState
		
		self.window.bind_all("<Key>", self.keyPressed)
		
		self.startGame()

		self.window.mainloop()

	def initView(self):
		self.canvas = tk.Canvas(self.window, bg="#666", height=GameBoard.SIZE_Y*SnakeGameView.SNAKE_WIDTH, width=GameBoard.SIZE_X*SnakeGameView.SNAKE_WIDTH)
		self.gameScoreLabel = tk.Label(self.window)
		self.gameInfoLabel = tk.Label(self.window)

	def setState(self, newState):
		self.currentState = newState
		newState.start()

	def startGame(self):
		self.setState(self.gameRunningState)

	def keyPressed(self, event):
		self.currentState.keyPressed(event)
		
a = SnakeGameView()
