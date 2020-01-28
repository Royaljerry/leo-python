import random
class Leg:
	def __init__(self):
		self.data_representation = {
			'side': '0011',
			'front': '0110'
		}

		self.direction = random.randint(0, 2)
		if self.direction == 0:
			self.direction = 'normal: ' + str(self.data_representation['side'])
		elif self.direction == 2:
			self.direction = 'reversed: ' + str(self.reverseString(self.data_representation['side']))
		elif self.direction == 1:
			self.direction = self.data_representation['front']

		print('leg created with direction ', self.direction)
		print('')
	
	# def calculate_direction(self, direction, representation):
	# 	print(direction)

	def reverseString(self, string):
		return string[::-1]