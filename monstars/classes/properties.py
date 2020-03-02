import json
from classes import utilities
from classes.monster import Monster

class Sizes:
	def __init__(self,data):
		self.head_length = data['head'][0]
		self.head_height = data['head'][1]

		self.body_length = data['body'][0]
		self.body_height = data['body'][1]

		self.pattern_length = data['pattern'][0]
		self.pattern_height = data['pattern'][1]
		
		self.arm_length = data['arm']['straight'][0]
		self.arm_height = data['arm']['straight'][1]
		
		self.palm_length = data['palm'][0]
		self.palm_height = data['palm'][1]

		self.foot_length = data['foot'][0]
		self.foot_height = data['foot'][1]

		self.leg_length = data['leg']['front'][0]
		self.leg_height = data['leg']['front'][1]

		self.cut_arm_length = self.arm_length - data['palm'][0]
		self.cut_arm_height = data['arm']['downwards'][1]

		self.cut_leg_length = data['leg']['left'][0]
		self.cut_leg_height = self.leg_height - data['foot'][1]
        
class Attributes:
	def __init__(self,data):
		self.rows = data['dimensions'][1]
		self.columns = data['dimensions'][0]
		self.monster_width = data['monster_size'][0]
		self.monster_height = data['monster_size'][1]

		self.gap = int(data['gap'][0])
		self.padding = int(data['padding'][0])
		self.image_width = (self.columns * self.monster_width) + ((self.columns - 1) * self.gap) + (self.padding * 2)
		self.image_height = (self.rows * self.monster_height) + ((self.rows - 1) * self.gap) + (self.padding * 2)

		self.pixel = utilities.get_real_pixel([self.monster_width, self.monster_height], [(2 * data['arm']['straight'][0]) +data['body'][0], data['head'][1] + data['body'][1] + data['leg']['front'][1]])
		self.ph = self.pixel[0] #pixels horizontally
		self.pv = self.pixel[1] #pixels vertically
