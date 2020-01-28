import random
class Leg:
	def __init__(self):
		self.data_representation = {
			'side': '0011',
			'front': '0110'
		}

		self._direction = random.randint(0, 2)
		if self._direction == 0:
			self.direction = self.data_representation['side']
		elif self._direction == 2:
			self.direction = self.reverseString(self.data_representation['side'])
		elif self._direction == 1:
			self.direction = self.data_representation['front']
		
		print('leg direction: ' + str(self.direction))
		print('')

	def reverseString(self, string):
		return string[::-1]