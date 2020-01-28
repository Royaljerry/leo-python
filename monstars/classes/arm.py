import random

class Arm:
	def __init__(self):
		
		self.data_representation = {
			'curved': '0010',
			'straight': '0011'
		}

		self._direction = random.randint(0, 2)
		if self._direction == 2:
			self.direction = self.reverseString(self.data_representation['curved'])
		elif self._direction == 0:
			self.direction = self.data_representation['curved']
		else: 
			self.direction = self.data_representation['straight']
		print('arm direction ', self.direction)

	def reverseString(self, string):
		return string[::-1]