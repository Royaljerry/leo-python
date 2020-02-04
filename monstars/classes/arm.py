import random

from classes import utilities

class Arm:
	def __init__(self):
		
		self.data_representation = {
			'curved': '0010',
			'straight': '0011'
		}

		self._direction = random.randint(0, 2)
		if self._direction == 2:
			self.direction = utilities.reverseString(self.data_representation['curved'])
		elif self._direction == 0:
			self.direction = self.data_representation['curved']
		else: 
			self.direction = self.data_representation['straight']
		print('arm direction ', self.direction)
