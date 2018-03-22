from State import *

class ShouldStartNewGameState(State):
	def __init__(self, view):
		self.view = view

	def render(self):
		self.view.startGame()

	def keyPressed(self, event):
		if event.keysym == 'space':
			self.view.startGame()