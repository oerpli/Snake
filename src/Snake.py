import random
import os
from enum import Enum
from collections import deque
from Direction import *

class Snake:
	INIT_SIZE = 3
	SPEED = 1

	def __init__(self, X, Y, initDirection):
		self.Score = 0
		self.Grow = False
		self.Direction = initDirection
		self.Segments = deque()
		for i in range(Snake.INIT_SIZE):
			self.Segments.append((X+i+1, Y))
		self.NewDirection = None
		self.DoesLive = True

	def IncrementScore(self):
		self.Score += 1

	def Kill(self):
		self.DoesLive = False

	def IsAlive(self):
		return self.DoesLive

	def Move(self):
		# Returns new position of front
		if self.NewDirection is not None:
			if Direction.ValidNewDirection(self.Direction,self.NewDirection):
				self.Direction = self.NewDirection
		# last = self.Segments.pop()
		new = Direction.AddToPoint(self.Segments[-1], self.Direction)
		# self.Segments.append(last)
		self.Segments.append(new)
		# end = None
		if not self.Grow:
			end = self.Segments.popleft()
		else:
			self.Grow = False
		return new # step successful

	def GetCoordinates(self):
		for elems in self.Segments:
			yield elems

	def IsSnake(self, coords, snake = None):
		if coords in self.GetCoordinates():
			if self == snake:
				if self.Segments[-1] == coords:
					return False
			return True