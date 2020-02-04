from classes import utilities

class Arm:
	def __init__(self):
		
		self.data_representation = {
			'curved': '0010',
			'straight': '0011'
		}

		self.straightness = utilities.get_straightness()
