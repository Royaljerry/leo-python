from classes import utilities

class Leg:
	def __init__(self):
		self.data_representation = [
			'left',
			'right',
			'front'
		]
		
		self.direction = self.data_representation[utilities.get_direction()]
