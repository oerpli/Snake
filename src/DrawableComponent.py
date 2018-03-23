from Drawable import *

class DrawableComponent(Drawable):
	def add(self, child): # default implementation, can be overridden
		raise NotImplementedError
	def remove(self,child): # def. impl
		raise NotImplementedError
	
	def childrenIterator(self): # def. impl
		raise NotImplementedError

	def Operation(self):
		raise NotImplementedError
