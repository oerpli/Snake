from GameBoard import *
from Direction import *

g = GameBoard()

def gaming(dir):
	r = g.Step(dir)
	print(r)

	
for d in [Direction.UP,None,Direction.LEFT,Direction.DOWN,None,None,None,None]:
	gaming(d)