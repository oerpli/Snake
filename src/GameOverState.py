from State import *

class GameOverState(State):
	def __init__(self, view):
		self.view = view

	def render(self):
		self.view.updateGameInfo(gameOver = True)

	def keyPressed(self, event):
		if event.keysym == 'space':
			self.view.startGame()