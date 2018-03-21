from Drawable import *
from RectangleDrawer import *

class Food(Drawable):
	def __init__(self, position):
		super().__init__()
		self.position = position
	def IsThere (self, position):
		return self.position == position

	def Draw(self):
		self.GetDrawer().Draw([self.position])