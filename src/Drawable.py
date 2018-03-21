class Drawable:
	def __init__(self):
		pass
	def InitDrawer(self,drawer):
		self.__drawer = drawer	
	def GetDrawer(self):
		return self.__drawer
	def Draw(self):
		raise NotImplementedError