from ColorGenerator import *
from pylab import cm
import matplotlib


class ColormapGenerator(ColorGenerator):
	index = 1
	colormaps = ['viridis', 'jet', 'magma', 'Spectral']

	def __init__(self, min=0.0, max=1.0, name='jet'):
		self.ncolors = 50
		cmap = cm.get_cmap(
			self.colormaps[ColormapGenerator.index], self.ncolors)  # PiYG
		ColormapGenerator.index = (
			ColormapGenerator.index+1) % len(ColormapGenerator.colormaps)
		self.colors = []
		for i in range(self.ncolors):
			rgb = cmap(i / self.ncolors)[:3]  # need rgb, not rgba
			self.colors.append(matplotlib.colors.rgb2hex(rgb))
		self.lastcolor = 0
		self.increment = 1

	def getNextColor(self):
		self.lastcolor = self.lastcolor + self.increment
		if self.lastcolor == 0 or self.lastcolor == self.ncolors-1:
			self.increment *= -1
		# print(self.lastcolor)
		# print(self.colors)
		return self.colors[self.lastcolor]
