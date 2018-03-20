from enum import Enum

class Direction(Enum):
	LEFT = 0
	RIGHT = 1
	UP = 2
	DOWN = 3


	@staticmethod
	def ValidNewDirection(old_dir, new_dir):
		if old_dir == Direction.LEFT and new_dir == Direction.RIGHT:
			return False
		if old_dir == Direction.UP and new_dir == Direction.DOWN:
			return False
		if new_dir == Direction.LEFT and old_dir == Direction.RIGHT:
			return False
		if new_dir == Direction.UP and old_dir == Direction.DOWN:
			return False
		return True

	@staticmethod
	def DirectionToVector(direction):
		if direction == Direction.LEFT:
			return (-1, 0)
		if direction == Direction.RIGHT:
			return (1, 0)
		if direction == Direction.UP:
			return (0, 1)
		if direction == Direction.DOWN:
			return (0, -1)
		raise Exception("WTF invalid direction")

	@staticmethod
	def AddToPoint(coords, dir):
		vec = Direction.DirectionToVector(dir)
		return (coords[0]+vec[0], coords[1]+vec[1])

	@staticmethod
	def MoveToPoint(c1, c2):
		# moves point c1 one step into direction of c2
		# if points overlap afterwards return only one, else both
		if c1[0] == c2[0]:
			a = (c1[0], c1[1] + (1 if c2[1]-c1[1] > 0 else -1))
		elif c1[1] == c2[1]:
			a = (c1[0] + (1 if c2[0]-c1[0] > 0 else -1), c1[1])
		else:
			raise Exception("WTF is going on here")
		output = [c2]  # always return c2
		if a != c2:  # if they are not the same also return the new end
			output.append(a)
		return output


