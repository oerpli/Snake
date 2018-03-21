class RectangleDrawer:
	def __init__(self, canvas, rectangleWidth):
		self.Width = rectangleWidth
		self.Canvas = canvas


	def GetColor(self):
		return "black"

	def Draw(self, rectangleIterator):
		for (x,y) in rectangleIterator:
			x *= self.Width
			y *= self.Width
			self.Canvas.create_rectangle(x, y, x + self.Width, y + self.Width, fill= self.GetColor(), width=0)


	def Colormaps(self):
		cmap = cm.get_cmap('viridis', 4)    # PiYG
		colors = []
		for i in range(cmap.N):
			rgb = cmap(i)[:3] # will return rgba, we take only first 3 so we get rgb
			colors.append(matplotlib.colors.rgb2hex(rgb))
		# colors = ["#ABFF19", "#E8C217", "#FF9526", "#E82C17", "#F968FF"]
	
		