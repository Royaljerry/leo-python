import random

class Head:
	def __init__(self):
		self.direction = random.randint(0, 2)
		print('head created with direction ', self.direction)