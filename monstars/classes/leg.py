import random
class Leg:
	def __init__(self):
		self.direction = random.randint(0, 2)
		print('leg created with direction ', self.direction)
