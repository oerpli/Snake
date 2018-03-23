from Drawable import *
from DrawableLeaf import *

class DrawableComposite(DrawableLeaf):
	def __init__(self):
		self.Children = []
	
	def add(self, child): # default implementation, can be overridden
		self.Children.append(child)
	
	def remove(self,child): # def. impl
		if child in self.Children:
			self.Children.remove(child)
			return True
		return False
	
	def childrenIterator(self): # def. impl
		for child in self.Children:
			yield child

	def Operation(self):
		self.Draw()
		for child in self.childrenIterator():
			child.Operation()
