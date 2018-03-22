from State import *

class GameOverState(State):
	def __init__(self, view):
		self.view = view

	def start(self):
		pass

	def keyPressed(self, event):
		if event.keysym == 'space':
			self.view.startGame()