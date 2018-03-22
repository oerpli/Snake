from SingleColorGenerator import *

class RectangleDrawer:
	def __init__(self, canvas, rectangleWidth, colorGenerator = None):
		self.Width = rectangleWidth
		self.Canvas = canvas

		self.ColorGenerator = colorGenerator if colorGenerator is not None else SingleColorGenerator()

	def GetColor(self):
		return self.ColorGenerator.getNextColor()

	def Draw(self, rectangleIterator):
		for (x,y) in rectangleIterator:
			x *= self.Width
			y *= self.Width
			self.Canvas.create_rectangle(x, y, x + self.Width, y + self.Width, fill= self.GetColor(), width=0)

