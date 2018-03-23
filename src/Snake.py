import random
import os
from enum import Enum
from collections import deque
from Direction import *
from RectangleDrawer import *
from DrawableComposite import *

class Snake(DrawableComposite):
	INIT_SIZE = 3
	SPEED = 1

	def __init__(self, X, Y, initDirection):
		super().__init__()
		self.Score = 0
		self.Grow = False
		self.Direction = initDirection
		self.Segments = deque()
		pos = (X,Y)
		for i in range(Snake.INIT_SIZE):
			pos = Direction.AddToPoint(pos,initDirection)
			self.Segments.append(pos)
		self.__NewDirection = None
		self.DoesLive = True

	def setNewDirection(self, newdir):
		self.__NewDirection = newdir

	def Draw(self):
		self.GetDrawer().Draw(self.Segments)

	def IncrementScore(self):
		self.Score += 1

	def Kill(self):
		self.DoesLive = False

	def IsAlive(self):
		return self.DoesLive

	def Move(self):
		# Returns new position of front
		if self.__NewDirection is not None:
			if Direction.ValidNewDirection(self.Direction,self.__NewDirection):
				self.Direction = self.__NewDirection
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

	def IsSnake(self, coords, ignoreHead = False):
		if ignoreHead:
			x = self.Segments.pop()
			r = coords in self.GetCoordinates()
			self.Segments.append(x)
			return r
		return coords in self.GetCoordinates()
		# if coords in self.GetCoordinates():
		# 	if self == snake:
		# 		if self.Segments[-1] == coords:
		# 			return False
		# 	return True