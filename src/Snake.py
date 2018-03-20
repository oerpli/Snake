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
		self.Direction = initDirection
		self.Segments = deque()
		for i in range(Snake.INIT_SIZE):
			self.Segments.append((X+i+1, Y))
		self.NewDirection = None

	def IncrementScore():
		self.Score += 1
	def Move(self, grow = False):
		# Returns tuple (old end of snake, new front of snake, doesLive)
		if self.NewDirection is not None:
			if Direction.ValidNewDirection(self.Direction,self.NewDirection):
				self.Direction = self.NewDirection
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