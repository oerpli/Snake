from State import *
from Direction import *
from RectangleDrawer import *
from BlinkingColorGenerator import *
from SingleColorGenerator import *
from ColormapGenerator import *
from GameBoard import *

class GameRunningState(State):
	def __init__(self, view, snakeWidth, gameLoopInterval):
		super().__init__()
		self.view = view
		self.window = view.window
		self.canvas = view.canvas
		self.snakeWidth = snakeWidth
		self.gameLoopInterval = gameLoopInterval
		self.Game = None
		self.numPlayers = 2
		self.foodDrawer = RectangleDrawer(
			self.canvas, self.snakeWidth, BlinkingColorGenerator())
		self.food = None

	def start(self):
		self.score = 0
		self.canvas.delete("all")

		self.Game = GameBoard(self.numPlayers)
		self.Game.Food.InitDrawer(self.foodDrawer)
		self.snakes = self.Game.GetSnakes()
		self.__registerKeys()

		colors = ["#ABFF19", "#E8C217", "#FF9526", "#E82C17", "#F968FF"]
		for (i, snake) in enumerate(self.snakes):
			drawer = RectangleDrawer(
				self.canvas, self.snakeWidth, ColormapGenerator())
			snake.InitDrawer(drawer)

		self.gameLoop()

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

		self.loopCall = self.window.after(self.gameLoopInterval, self.gameLoop)

	def handleGameOver(self):
		self.window.after_cancel(self.loopCall)
		self.updateGameInfo(gameOver=True)
		self.view.setState(self.view.gameOverState)

	def updateGameInfo(self, score=0, gameOver=False):
		self.window.title("Snake - {} player{}".format(self.numPlayers,
												 '' if self.numPlayers == 1 else 's'))
		self.view.gameScoreLabel.config(text=self.getScoreString())

		if gameOver:
			self.view.gameInfoLabel.config(
				text="Game Over! - press space to restart", fg="red")
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

	def __registerKeys(self):
		self.registerCommand('space',self.handleGameOver)
		for i in range(1,5):
			self.registerCommand(str(i), self.__changePlayerNumber,i)
		keyBindings = [['Up', 'Down', 'Left', 'Right'],
					   list('wsad'), list('ikjl'), list('tgfh')]
		self.keyDict = dict()
		zipped = zip(self.snakes, keyBindings)
		for snake, keys in zipped:
			self.__registerPlayerKeys(snake, keys)

	def __registerPlayerKeys(self, snake, keys):
		# keys should be list of key events in the order:
		# UP DOWN LEFT RIGHT (WSAD)
		print(snake)
		print(keys)
		for (key, dir) in zip(keys, [Direction.DOWN, Direction.UP, Direction.LEFT, Direction.RIGHT]):
			print(key,dir)
			self.registerCommand(key, snake.setNewDirection,dir)

	def __changePlayerNumber(self,num):
		self.window.after_cancel(self.loopCall)
		self.numPlayers = num
		self.start()
