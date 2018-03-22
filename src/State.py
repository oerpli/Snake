from Commander import *

class State():
	def __init__(self):
		self.Commmander = Commander()

	def start(self):
		pass

	def registerCommand(self,key,function, arg = None):
		self.Commmander.registerCommand(key,function, arg)

	def keyPressed(self, event):
		self.Commmander.runCommand(event.keysym)