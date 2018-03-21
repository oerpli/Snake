import random
from Snake import *
from Direction import *

class GameBoard:
	SIZE_X = 30
	SIZE_Y = 30

	def __init__(self, numSnakes = 3):
		self.Snakes = []
		(cX,cY) = (GameBoard.SIZE_X // 2, GameBoard.SIZE_Y // 2)

		dirs = [Direction.LEFT,Direction.RIGHT,Direction.UP,Direction.DOWN]
		self.Snakes = [Snake(cX,cY,initDir) for initDir in dirs[:numSnakes]]
		self.Food = (0,0)
		self.GenerateFood()
		self.Grow = False
		self.score = 0
	
	def GetSnakes(self):
		return self.Snakes

	def Step(self):
		# Return information about new gamestate:
		# e if a snakeblock is removed (coords)
		# n if snake grows (coords)
		# Bool if gamestate is still valid
		# nf = None or coords of new food
		newFronts = []
		newFood = False
		for snake in self.Snakes:
			newFront = snake.Move()
			newFronts.append(newFront)
			newFront = self.Reappear(snake,newFront)
			if newFront == self.Food:
				snake.Grow = True
				snake.IncrementScore()	
				newFood = True
			if not self.IsValidPoint(newFront, True):
				snake.Kill()
		if newFood:
			self.GenerateFood()
		for i,e in enumerate(newFronts):
			for j,f in enumerate(newFronts):
				if i < j:
					if e == f:
						self.Snakes[i].Kill()
						self.Snakes[j].Kill()
		return (self.Snakes,self.Food)

	def Reappear(self,snake,position):
		(x,y) = position
		x = (x + GameBoard.SIZE_X) % GameBoard.SIZE_X
		y = (y + GameBoard.SIZE_Y) % GameBoard.SIZE_Y
		snake.Segments[-1] = (x,y)
		return (x,y)
		

	def IsValidPoint(self,point, ignoreHead = False):
		for snake in self.Snakes:
			if snake.IsSnake(point, ignoreHead):
				return False
		# if point[0] < 0 or point[1] < 0:
		# 	return False
		# if point[0] >= GameBoard.SIZE_X or point[1] >= GameBoard.SIZE_Y:
		# 	return False
		return True

	def CheckCrashes(self,snake,coord):
		for s in self.Snakes:
			if s is snake:
				continue

	def SamplePoint(self):
		while True:  # very slow if snake is long
			x = random.randint(0, GameBoard.SIZE_X-1)
			y = random.randint(0, GameBoard.SIZE_Y-1)
			if self.IsValidPoint((x,y)):
				return (x, y)

	def GenerateFood(self):
		self.Food = self.SamplePoint()
		return self.Food
