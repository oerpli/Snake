import random
import os
from enum import Enum
from collections import deque
from Direction import *

class Snake:
	INIT_SIZE = 5
	SPEED = 1

	def __init__(self, X, Y):
		self.Direction = Direction.RIGHT
		self.Segments = deque()
		for i in range(Snake.INIT_SIZE):
			self.Segments.appendleft((X-i, Y))

	def Move(self, direction = None, grow=False):
		if direction is not None:
			self.Direction = direction
		last = self.Segments.pop()
		new = Direction.AddToPoint(last, self.Direction)
		self.Segments.append(last)
		if new in self.Segments:
			return (None,new,False) # snake died
		self.Segments.append(new)
		end = None
		if not grow:
			end = self.Segments.popleft()
		return (end,new,True) # step successful

	def GetCoordinates(self):
		for elems in self.Segments:
			yield elems

	def IsSnake(self, coords):
		return coords in self.GetCoordinates()