import random
import os
from enum import Enum
from collections import deque


class Direction(Enum):
	LEFT = 0
	RIGHT = 1
	UP = 2
	DOWN = 3

	@staticmethod
	def DirectionToVector(dir):
		print(dir)
		if dir == Direction.LEFT:
			return (-1, 0)
		if dir == Direction.RIGHT:
			return (1, 0)
		if dir == Direction.UP:
			return (0, 1)
		if dir == Direction.Down:
			return (0, -1)
		raise Exception("WTF invalid direction")

	@staticmethod
	def AddToPoint(coords, dir):
		vec = Direction.DirectionToVector(dir)
		return (coords[0]+vec[0],coords[1]+vec[1])

	@staticmethod
	def MoveToPoint(c1, c2):
		print(c1,c2)
		# moves point c1 one step into direction of c2
		# if points overlap afterwards return only one, else both
		if c1[0] == c2[0]:
			a = (c1[0], c1[1] + (1 if c2[1]-c1[1] > 0 else -1))
		elif c1[1] == c2[1]:
			a = (c1[0] + (1 if c2[0]-c1[0] > 0 else -1), c1[1])
		else:
			raise Exception("WTF is going on here")
		output = [c2]  # always return c2
		if a != c2:  # if they are not the same also return the new end
			output.append(a)
		print(output)
		return output


class Snake:
	INIT_SIZE = 5
	SPEED = 1

	def __init__(self, X, Y):
		self.Direction = Direction.RIGHT
		self.Segments = deque()
		self.Segments.appendleft((X-Snake.INIT_SIZE, Y))
		self.Segments.append((X, Y))

	def Move(self, direction, grow=False):
		# in case of direction change
		# first add point before change to segments
		# then update current position

		# impossibleDirs = [
		# 	(Direction.LEFT, Direction.RIGHT),
		# 	(Direction.UP, Direction.DOWN),
		# 	(Direction.RIGHT, Direction.LEFT),
		# 	(Direction.DOWN, Direction.UP)
		# ]
		# # if user tries to make a 180 turn ignore input alltogether
		# if (direction, self.Direction) in impossibleDirs:
		# 	direction = self.Direction

		# pop last position, if direction changed add it again
		# else add direction vector to it and add it again afterwards
		last = self.Segments.pop()
		if direction != self.Direction:
			self.Segments.append(last)
		self.Direction = direction
		new = Direction.AddToPoint(last, direction)
		self.Segments.append(new)

		if not grow:
			end1 = self.Segments.popleft()
			end2 = self.Segments.popleft()
			for newend in Direction.MoveToPoint(end1, end2):
				self.Segments.appendleft(newend)
		print(self.Segments)

	def GetCoordinates(self):
		for elems in self.Segments:
			yield elems

	def IsSnake(self, coords):
		return coords in self.GetCoordinates()


class GameBoard:
	SIZE_X = 21
	SIZE_Y = 21

	def __init__(self):
		self.Snake = Snake(GameBoard.SIZE_X // 2, GameBoard.SIZE_Y // 2)
		self.GenerateFood()

	def ClearConsole(self):
		os.system('cls' if os.name == 'nt' else 'clear')

	def Print(self):
		# self.ClearConsole()
		print(self)

	def SamplePoint(self):
		while True:
			x = random.randint(0, GameBoard.SIZE_X-1)
			y = random.randint(0, GameBoard.SIZE_Y-1)
			if not self.Snake.IsSnake((x, y)):
				return (x, y)

	def GenerateFood(self):
		self.Food = self.SamplePoint()

	def __str__(self):
		fields = [list("_"*GameBoard.SIZE_Y) for _ in range(GameBoard.SIZE_X)]
		for (x, y) in self.Snake.GetCoordinates():
			fields[y][x] = 'X'
		(fX, fY) = self.Food
		fields[fY][fX] = 'O'
		return "\n".join(["".join(line) for line in reversed(fields)])


g = GameBoard()
g.Print()

g.Snake.Move(Direction.UP)
g.Print()
g.Snake.Move(Direction.UP)
g.Print()
g.Snake.Move(Direction.LEFT)
g.Print()
g.Snake.Move(Direction.LEFT)
g.Print()
g.Snake.Move(Direction.LEFT)
g.Print()
g.Snake.Move(Direction.LEFT)
g.Print()
g.Snake.Move(Direction.LEFT)
g.Print()
