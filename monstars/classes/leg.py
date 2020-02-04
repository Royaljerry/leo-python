from classes import utilities

class Leg:
	def __init__(self):
		self.data_representation = {
			'side': '0011',
			'front': '0110'
		}
		
		self.direction = utilities.get_direction()
