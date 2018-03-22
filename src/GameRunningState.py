from State import *
from Direction import *
from RectangleDrawer import *
from BlinkingColorGenerator import *
from SingleColorGenerator import *
from GameBoard import *

class GameRunningState(State):
	def __init__(self, view, snakeWidth, gameLoopInterval):
		self.view = view
		self.window = view.window
		self.canvas = view.canvas
		self.snakeWidth = snakeWidth
		self.gameLoopInterval = gameLoopInterval
		self.Game = None

		self.initKeyDict()
		self.continueLoop = True
		self.numPlayers = 2
		self.foodDrawer = RectangleDrawer(self.canvas, self.snakeWidth, BlinkingColorGenerator())
		self.food = None

	def start(self):
		self.score = 0
		self.canvas.delete("all")
		
		self.Game = GameBoard(self.numPlayers)
		self.Game.Food.InitDrawer(self.foodDrawer)
		self.snakes = self.Game.GetSnakes()

		colors = ["#ABFF19", "#E8C217", "#FF9526", "#E82C17", "#F968FF"]
		for (i, snake) in enumerate(self.snakes):
			drawer = RectangleDrawer(self.canvas,self.snakeWidth,SingleColorGenerator(colors[i]))
			snake.InitDrawer(drawer)

		self.gameLoop()
		self.continueLoop = True

	def gameLoop(self):
		(self.snakes, newFood) = self.Game.Step()
		if self.food is not newFood:
			self.food = newFood
			self.food.InitDrawer(self.foodDrawer)
		for snake in self.snakes:
			if not snake.IsAlive():
				self.handleGameOver()
				return
		
		self.canvas.delete("all")
		for snake in self.snakes:
			snake.Draw()
		self.food.Draw()
		self.canvas.pack()

		self.updateGameInfo()

		if self.continueLoop:
			self.window.after(self.gameLoopInterval, self.gameLoop)

	def keyPressed(self, event):
		if event.keysym == '1':
			self.numPlayers = 1
			self.continueLoop = False
			self.start()
			return
		if event.keysym == '2':
			self.numPlayers = 2
			self.continueLoop = False
			self.start()
			return
		if event.keysym == '3':
			self.numPlayers = 3
			self.continueLoop = False
			self.start()
			return
		if event.keysym == '4':
			self.numPlayers = 4
			self.continueLoop = False
			self.start()
			return
		
		key = self.KeyDict.get(event.keysym, None)
		if key is not None:
			(snake,dir) = key
			self.snakes[snake].NewDirection = dir

	def handleGameOver(self):
		self.updateGameInfo(gameOver = True)
		self.view.setState(self.view.gameOverState)

	def updateGameInfo(self, score = 0, gameOver = False):
		self.window.title("Snake - {} {}".format(self.numPlayers, 'player' if self.numPlayers == 1 else 'players'))
		self.view.gameScoreLabel.config(text = self.getScoreString())

		if gameOver:
			self.view.gameInfoLabel.config(text="Game Over! - press space to restart", fg="red")
		else:
			self.view.gameInfoLabel.config(text="Game running", fg="black")
			
		self.view.gameInfoLabel.pack()
		self.view.gameScoreLabel.pack()

	def getScoreString(self):
		i = 65
		scoresStrings = []
		for snake in self.snakes:
			scoresStrings.append("Snake {}: {}".format(chr(i), snake.Score))
			i += 1

		return "; ".join(scoresStrings)

	def initKeyDict(self):
		players = [['Up', 'Down', 'Left', 'Right'],
				list('wsad'), list('ikjl'), list('tgfh')]
		self.keyDict = dict()
		for i, e in enumerate(players[:self.view.numPlayers]):
			playerdict = self.playerKeyDict(e, i)
			self.keyDict = {**self.keyDict, **playerdict}

	def playerKeyDict(self, keys, playerNumber):
		# keys should be list of key events in the order:
		# UP DOWN LEFT RIGHT (WSAD)
		playerdict = dict()
		for (key, dir) in zip(keys, [Direction.DOWN, Direction.UP, Direction.LEFT, Direction.RIGHT]):
			playerdict[key] = (playerNumber, dir)
		return playerdict
