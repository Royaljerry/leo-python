import random

data_representation = {
	'side':['0011'] ,
	'front':['0110']
}
class Leg:
	def __init__(self):
		self.direction = random.randint(0, 2)
		if self.direction == 2 or self.direction == 0:
			self.direction = data_representation['front']
		else: 
			self.direction = data_representation['side']
		print('leg created with direction ', self.direction)
