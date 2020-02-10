from classes import utilities

class Arm:
	def __init__(self):
		
		self.data_representation = [
			'downwards',
			'upwards',
			'straight'
		]

		self.straightness = utilities.get_straightness()
