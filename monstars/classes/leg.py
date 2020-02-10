from classes import utilities

class Leg:
	def __init__(self):
		self.data_representation = [
			'left',
			'right',
			'front'
		]
		
		self.direction = utilities.get_direction()
