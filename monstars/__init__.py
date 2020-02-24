#!/usr/bin/env python3

import random
import json
from PIL import Image, ImageDraw

from classes import utilities
from classes.monster import Monster

data = ''
monsters = []

def create_monsters(monsters_hor, monsters_ver):
	for row in range(monsters_ver):
		for column in range(monsters_hor):
			monster = Monster()
			monsters.append(monster)

def main():
	with open("data/data.json", "r") as read_file:

#create image

		data = json.load(read_file)
		read_file.close()
	create_monsters(data['dimensions'][0], data['dimensions'][1])
	image_width = (data['dimensions'][0] * data['monster_size'][0]) + (
			int((data['dimensions'][0]) - 1) * int(data['gap'])) + int((data['padding'] * 2))
	image_height = (data['dimensions'][1] * data['monster_size'][1]) + (
			(data['dimensions'][1] - 1) * int(data['gap'])) + int((data['padding'] * 2))
	monster_image = Image.new('RGB', (image_width, image_height), utilities.hsl(100, 50, 50))
	monster_draw = ImageDraw.Draw(monster_image)

	gap = int(data['gap'])
	padding = int(data['padding'])
	monster_width = data['monster_size'][0]
	monster_height = data['monster_size'][1]

	# Calculate pixel size

	pixels_hor = (2 * data['arm']['straight'][0]) +data['body'][0]
	pixels_ver = data['head'][1] + data['body'][1] + data['leg']['front'][1]
	pixel = utilities.get_real_pixel(data['monster_size'], [pixels_hor, pixels_ver])
	pixel_hor = pixel[0]
	pixel_ver = pixel[1]

	print(pixel_hor, pixel_ver)
	# Calculate body parts

	body_x1 = data['arm']['straight'][0] *pixel_hor
	body_y1 = data['head'][0] * pixel_ver
	body_x2 = body_x1 + data['body'][0] * pixel_hor 
	body_y2 = body_y1 + data['body'][1] * pixel_ver

	head_y1 = 0
	head_y2 = head_y1 + data['head'][1] * pixel_ver



	for index, monster in enumerate(monsters, start=0):

		current_column = index % data['dimensions'][0]
		current_row = int(index / data['dimensions'][0])

		# Calculate dimensions

		coord_left_top_x = (padding + (current_column * (monster_width + gap)) )  * pixel_hor
		coord_left_top_y = (padding + (current_row * (monster_height + gap)))  * pixel_ver 
		coord_right_bot_x = (coord_left_top_x + monster_width )  * pixel_hor
		coord_right_bot_y = (coord_left_top_y + monster_height ) * pixel_ver

		body_right_x = coord_right_bot_x - data['arm']['straight'][0] * pixel_hor
		body_left_x = coord_left_top_x + data['arm']['straight'][0] * pixel_ver

		#calculate body parts

		if monster.head.direction == 'left':
			head_x1 = 0
			head_x2 = head_x1 + data['head'][0]* pixel_hor
		elif monster.head.direction == 'right':
			head_x1 = (coord_right_bot_x - coord_left_top_x-data['head'][0]- data['arm']['straight'][0]*2) * pixel_hor
			head_x2 = head_x1 + data['head'][0]*pixel_hor
		else:
			head_x1 = data['body'][0] * pixel_hor / 2 - data['head'][0] *pixel_hor / 2
			head_x2 = head_x1 + data['head'][0] *pixel_hor

		larm_y1 = data['head'][1] + random.randint(0, data['body'][1]-data['arm']['straight'][1])
		larm_y2 = larm_y1 + data['arm']['straight'][1]

		if monster.left_arm.direction == 'straight':
			larm_x1 = 0
			larm_x2 = larm_x1 + data['arm']['straight'][0] *pixel_hor
		else: 
			larm_x1 = data['palm'][0]
			larm_x2 = larm_x1 + data['arm']['downwards'][0]
			if monster.left_arm.direction == 'downwards':
				monster_draw.rectangle([coord_left_top_x, coord_left_top_y + larm_y1 +data['arm']['downwards'][1], coord_left_top_x + larm_x1, coord_left_top_y + larm_y2 + data['arm']['downwards'][1] ], fill = 'blue', outline=None)
			else:
				monster_draw.rectangle([coord_left_top_x, coord_left_top_y + larm_y1-data['arm']['upwards'][1], coord_left_top_x + larm_x1, coord_left_top_y + larm_y1], fill = 'blue', outline=None)

		rarm_y1 = data['head'][1] + random.randint(0, data['body'][1]-data['arm']['straight'][1])
		rarm_y2 = rarm_y1 + data['arm']['straight'][1]
		rarm_x1 = body_right_x 

		if monster.right_arm.direction == 'straight':

			rarm_x2 = rarm_x1 + data['arm']['straight'][0]*pixel_hor
		else: 
			rarm_x2 = rarm_x1 + data['arm']['downwards'][0]*pixel_hor

			if monster.left_arm.direction == 'downwards':
				monster_draw.rectangle([rarm_x1 + data['arm']['downwards'][0], coord_left_top_y + rarm_y2, rarm_x1 + data['arm']['downwards'][0] + data['palm'][0], coord_left_top_y + rarm_y2 + data['palm'][1] ], fill = 'blue', outline=None)
			else: 
				monster_draw.rectangle([rarm_x1 + data['arm']['downwards'][0], coord_left_top_y + rarm_y2, rarm_x1 + data['arm']['downwards'][0] + data['palm'][0], coord_left_top_y + rarm_y2 + data['palm'][1] ], fill = 'blue', outline=None)	

		body_bot_y = coord_left_top_y + data['head'][1]*pixel_ver + data['body'][1] * pixel_ver


		leg_x1 = body_left_x + (data['body'][0] /6 * pixel_hor)
		leg_x2 = leg_x1 + data['leg']['front'][0] * pixel_hor
		leg_y1 = body_bot_y 

		if monster.leg.direction == 'front':
			leg_y2 = leg_y1 + data['leg']['front'][1] *pixel_ver

			monster_draw.rectangle([leg_x1, leg_y1, leg_x2, leg_y2], fill = 'blue', outline= None)
			
			leg_x1 = body_left_x + (data['body'][0] /6* 4 * pixel_hor)
			leg_x2 = leg_x1 + data['leg']['front'][0] * pixel_hor

			monster_draw.rectangle([leg_x1, leg_y1, leg_x2, leg_y2], fill = 'blue', outline=None)

		if monster.leg.direction == 'right':

			leg_y2 = body_bot_y + data['leg']['right'][1]
			monster_draw.rectangle([leg_x1, leg_y1, leg_x2, leg_y2],fill = 'blue', outline=None )
			monster_draw.rectangle([leg_x2, leg_y2, leg_x2 + data['palm'][0]*pixel_hor, leg_y2+ data['palm'][1]* pixel_ver], fill= 'blue' )

			leg_x1 = body_left_x + (data['body'][0] /6* 4 * pixel_hor)
			leg_x2 = leg_x1 + data['leg']['right'][0] * pixel_hor

			monster_draw.rectangle([leg_x1, leg_y1, leg_x2, leg_y2],fill = 'blue', outline=None )
			monster_draw.rectangle([leg_x2, leg_y2, leg_x2 + data['palm'][0]*pixel_hor, leg_y2+ data['palm'][1]* pixel_ver], fill= 'blue' )

		elif monster.leg.direction == 'left': 
			leg_y2 = body_bot_y + data['leg']['left'][1]

			monster_draw.rectangle([leg_x1, leg_y1, leg_x2, leg_y2],fill = 'blue', outline=None )
			monster_draw.rectangle([leg_x1 - data['palm'][0]*pixel_hor, leg_y2, leg_x1, leg_y2+ data['palm'][1]* pixel_ver], fill= 'blue' , outline=None)

			leg_x1 = body_left_x + (data['body'][0] /6* 4 * pixel_hor)
			leg_x2 = leg_x1 + data['leg']['right'][0] * pixel_hor

			monster_draw.rectangle([leg_x1, leg_y1, leg_x2, leg_y2],fill = 'blue', outline=None )
			monster_draw.rectangle([leg_x1 - data['palm'][0]*pixel_hor, leg_y2, leg_x1, leg_y2+ data['palm'][1]* pixel_ver], fill= 'blue' , outline=None)
		#draw

		# monster_draw.rectangle([coord_left_top_x, coord_left_top_y, coord_right_bot_x, coord_right_bot_y], fill=None, outline=None)

		monster_draw.rectangle([coord_left_top_x + body_x1, coord_left_top_y +body_y1 ,coord_left_top_x + body_x2,coord_left_top_y + body_y2],fill='blue',outline = None, width=0)
		
		monster_draw.rectangle([body_left_x + head_x1, coord_left_top_y + head_y1, body_left_x + head_x2, coord_left_top_y + head_y2] , fill = 'blue')

		monster_draw.rectangle([coord_left_top_x + larm_x1,coord_left_top_y + larm_y1,coord_left_top_x + larm_x2,coord_left_top_y + larm_y2], fill = 'blue', outline=None)

		monster_draw.rectangle([rarm_x1, coord_left_top_y + rarm_y1, rarm_x2, coord_left_top_y + rarm_y2], fill = 'blue', outline=None)







		
	monster_image.show()
if __name__ == '__main__':
	main()
