import random

class Arm:
	def __init__(self):
		
		self.data_representation = {
			'curved': ['0010'] ,
			'straight': ['0011']
		}

		self.direction = random.randint(0, 2)
		if self.direction == 2 or self.direction == 0:
			self.direction = self.data_representation['curved']
		else: 
			self.direction = self.data_representation['straight']
		print('arm created with direction ', self.direction)
