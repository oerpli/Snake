from State import *

class GameOverState(State):
	def __init__(self, view):
		super().__init__()
		self.view = view
		self.registerCommand('space',self.view.startGame)

	def start(self):
		pass