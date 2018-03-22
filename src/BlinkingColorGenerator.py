from ColorGenerator import *


class BlinkingColorGenerator(ColorGenerator):
	def __init__(self, colors = None, color2 = None):
		if colors is None and color2 is None:
			self.colors = ["#f00","#000"]
		elif color2 is not None:
			self.colors = [colors,color2]
		else:
			self.colors = colors
		self.currentColor = 0

	def getNextColor(self):
		self.currentColor = (self.currentColor + 1) % len(self.colors)
		return self.colors[self.currentColor]
