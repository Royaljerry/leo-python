import random

from classes import utilities

class Head:
	def __init__(self):

		self.data_representation = {
			'side': '0011' ,
			'front': '0110'
		}

		self._direction = random.randint(0, 2)

		if self._direction == 2:
			self.direction = utilities.reverseString(self.data_representation['side'])
		elif self._direction == 0:
			self.direction = self.data_representation['side']
		elif self._direction == 1: 
			self.direction = self.data_representation['front']
		print('head direction ', self.direction)
