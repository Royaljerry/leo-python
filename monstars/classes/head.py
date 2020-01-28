import random

class Head:
	def __init__(self):

		self.data_representation = {
			'side': ['0011'] ,
			'front': ['0110']
		}

		self.direction = random.randint(0, 2)
		if self.direction == 2 or self.direction == 0:
			self.direction = self.data_representation['front']
		else: 
			self.direction = self.data_representation['side']
		print('head created with direction ', self.direction)