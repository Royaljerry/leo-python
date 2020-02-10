from classes import utilities

class Arm:
	def __init__(self):
		
		self.data_representation = [
			'downwards',
			'upwards',
			'straight'
		]

		self.direction = self.data_representation[utilities.get_direction()]
