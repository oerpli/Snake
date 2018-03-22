class Commander:
	def __init__(self):
		self.Commands = dict()

	def registerCommand(self, key, function):
		self.Commands[key] = function

	def runCommand(self, key):
		cmd = self.Commands.get(key,None)
		if cmd:
			cmd()