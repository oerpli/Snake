class Commander:
	def __init__(self):
		self.Commands = dict()

	def registerCommand(self, key, function, arg = None):
		self.Commands[key] = (function,arg)

	def runCommand(self, key):
		cmd = self.Commands.get(key,None)
		if cmd:
			(fn,arg) = cmd
			if arg:
				fn(arg)
			else:
				fn()
