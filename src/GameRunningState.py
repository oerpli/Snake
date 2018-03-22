from State import *
from Direction import *

class GameRunningState(State):
	def __init__(self, view):
		self.view = view
		self.initKeyDict()

	def render(self):
		(self.view.snakes, newFood) = self.view.Game.Step()
		if self.view.food is not newFood:
			self.view.food = newFood
			self.view.food.InitDrawer(self.view.foodDrawer)
		for snake in self.view.snakes:
			if not snake.IsAlive():
				self.view.handleGameOver()
				return
		
		self.view.canvas.delete("all")
		for snake in self.view.snakes:
			snake.Draw()
		self.view.food.Draw()
		self.view.canvas.pack()

		self.view.updateGameInfo()

	def keyPressed(self, event):
		if event.keysym == '1':
			self.view.numPlayers = 1
			self.view.currentState = self.view.shouldStartNewGameState
			return
		if event.keysym == '2':
			self.view.numPlayers = 2
			self.view.currentState = self.view.shouldStartNewGameState
			return
		if event.keysym == '3':
			self.view.numPlayers = 3
			self.view.currentState = self.view.shouldStartNewGameState
			return
		if event.keysym == '4':
			self.view.numPlayers = 4
			self.view.currentState = self.view.shouldStartNewGameState
			return
		
		key = self.KeyDict.get(event.keysym, None)
		if key is not None:
			(snake,dir) = key
			self.view.snakes[snake].NewDirection = dir

	def initKeyDict(self):
		P0 = ['Up','Down','Left','Right']
		P1 = list('wsad')
		P2 = list('ikjl')
		P3 = list('tgfh')
		p0d = self.playerKeyDict(P0,0)
		p1d = self.playerKeyDict(P1,1)
		p2d = self.playerKeyDict(P2,2)
		p3d = self.playerKeyDict(P3,3)
		self.KeyDict = {**p0d, **p1d, **p2d, **p3d}

	def playerKeyDict(self, keys, playerNumber):
		# keys should be list of key events in the order:
		# UP DOWN LEFT RIGHT (WSAD)
		playerdict = dict()
		for (key,dir) in zip(keys,[Direction.DOWN,Direction.UP,Direction.LEFT,Direction.RIGHT]):
			playerdict[key] = (playerNumber,dir)
		return playerdict