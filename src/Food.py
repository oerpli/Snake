from DrawableLeaf import *
from RectangleDrawer import *

class Food(DrawableLeaf):
	def __init__(self, position):
		super().__init__()
		self.position = position
	def IsThere (self, position):
		return self.position == position

	def Draw(self):
		self.GetDrawer().Draw([self.position])