import random
class Leg:
	def __init__(self):
		self.data_representation = {
			'side': '0011',
			'front': '0110'
		}

		self.direction = random.randint(0, 2)
		if self.direction == 2 or self.direction == 0:
			self.direction = self.data_representation['side']
			print('normal: ' + str(self.direction))
			print('reversed: ' + str(self.reverseString(self.direction)))
		else: 
			self.direction = self.data_representation['front']
		print('leg created with direction ', self.direction)
	#print(calculate_direction(direction, data_representation))
	
	def calculate_direction(self, direction, representation):
		print(direction)

	def reverseString(self, string):
		return string[::-1]