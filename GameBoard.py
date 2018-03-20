import random
from Snake import *
from Direction import *

class GameBoard:
	SIZE_X = 30
	SIZE_Y = 30

	def __init__(self):
		self.Snake = Snake(GameBoard.SIZE_X // 2, GameBoard.SIZE_Y // 2)
		self.Food = (0,0)
		self.GenerateFood()
		self.Grow = False
		self.score = 0
	
	def ClearConsole(self):
		os.system('cls' if os.name == 'nt' else 'clear')

	def Print(self):
		# self.ClearConsole()
		print(self)

	def Step(self, dir = None):
		# Return information about new gamestate:
		# e if a snakeblock is removed (coords)
		# n if snake grows (coords)
		# Bool if gamestate is still valid
		# nf = None or coords of new food

		(oldEnd, newFront, doesLive) = self.Snake.Move(dir, self.Grow)
		self.Grow = False
		newFood = None
		if newFront == self.Food:
			self.Grow = True
			self.GenerateFood()
			newFood = self.Food
  		newFront = self.Reappear(newFront)
			self.score += 1	

		doesLive = doesLive and self.IsValidPoint(newFront)

		return (oldEnd,newFront,doesLive,self.score,newFood)

	def Reappear(self,position):
		(x,y) = position
		x = (x + GameBoard.SIZE_X)  
		y = (y + GameBoard.SIZE_Y)
		self.Snake.Segments[-1] = (x,y)
		return (x,y)
		

	def IsValidPoint(self,point):
		if point[0] < 0 or point[1] < 0:
			return False
		if point[0] >= GameBoard.SIZE_X or point[1] >= GameBoard.SIZE_Y:
			return False
		return True

	def SamplePoint(self):
		while True:  # very slow if snake is long
			x = random.randint(0, GameBoard.SIZE_X-1)
			y = random.randint(0, GameBoard.SIZE_Y-1)
			if not self.Snake.IsSnake((x, y)):
				return (x, y)

	def GenerateFood(self):
		self.Food = self.SamplePoint()

	def __str__(self): # printer for debugging in console
		fields = [list("_"*GameBoard.SIZE_Y) for _ in range(GameBoard.SIZE_X)]
		for (x, y) in self.Snake.GetCoordinates():
			fields[y][x] = 'X'
		(fX, fY) = self.Food
		fields[fY][fX] = 'O'
		return "\n".join(["".join(line) for line in reversed(fields)])