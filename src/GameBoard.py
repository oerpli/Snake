import random
from Snake import *
from Direction import *

class GameBoard:
	SIZE_X = 30
	SIZE_Y = 30

	def __init__(self, numSnakes = 2):
		self.Snakes = []
		(cX,cY) = (GameBoard.SIZE_X // 2, GameBoard.SIZE_Y // 2)

		dirs = [Direction.LEFT,Direction.RIGHT,Direction.UP,Direction.DOWN]
		self.Snakes = [Snake(cX,cY,initDir) for initDir in dirs[:numSnakes]]
		self.Food = (0,0)
		self.GenerateFood()
		self.Grow = False
		self.score = 0
	
	def Step(self):
		# Return information about new gamestate:
		# e if a snakeblock is removed (coords)
		# n if snake grows (coords)
		# Bool if gamestate is still valid
		# nf = None or coords of new food

		newFood = None
		for snake in self.Snakes:
			(oldEnd, newFront, doesLive) = snake.Move(self.Grow)
			self.Grow = False
			if newFront == self.Food:
				self.Grow = True
				self.GenerateFood()
				newFood = self.Food
				snake.IncrementScore()	
			newFront = self.Reappear(snake,newFront)
			doesLive = doesLive and self.IsValidPoint(newFront)
		return (self.Snakes,newFood)

	def Reappear(self,snake,position):
		(x,y) = position
		x = (x + GameBoard.SIZE_X) % GameBoard.SIZE_X
		y = (y + GameBoard.SIZE_Y) % GameBoard.SIZE_Y
		snake.Segments[-1] = (x,y)
		return (x,y)
		

	def IsValidPoint(self,point):
		for snake in self.Snakes:
			if snake.IsSnake(point):
				return False
		if point[0] < 0 or point[1] < 0:
			return False
		if point[0] >= GameBoard.SIZE_X or point[1] >= GameBoard.SIZE_Y:
			return False
		return True

	def SamplePoint(self):
		while True:  # very slow if snake is long
			x = random.randint(0, GameBoard.SIZE_X-1)
			y = random.randint(0, GameBoard.SIZE_Y-1)
			if self.IsValidPoint((x,y)):
				return (x, y)

	def GenerateFood(self):
		self.Food = self.SamplePoint()