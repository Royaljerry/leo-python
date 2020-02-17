#!/usr/bin/env python3

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
		data = json.load(read_file)
		read_file.close()
	create_monsters(data['dimensions'][0], data['dimensions'][1])
	image_width = (data['dimensions'][0] * data['monster_size'][0]) + (
			int((data['dimensions'][0]) - 1) * int(data['gap'])) + int((data['padding'] * 2))
	image_height = (data['dimensions'][1] * data['monster_size'][1]) + (
			(data['dimensions'][1] - 1) * int(data['gap'])) + int((data['padding'] * 2))
	monster_image = Image.new('RGB', (image_width, image_height), utilities.hsl(100, 50, 50))
	monster_draw = ImageDraw.Draw(monster_image)

	index = 0
	gap = int(data['gap'])
	padding = int(data['padding'])
	monster_width = data['monster_size'][0]
	monster_height = data['monster_size'][1]
	for monster in monsters:
		left_arm = data['arm'][monster.left_arm.direction]
		right_arm = data['arm'][monster.right_arm.direction]
		head = data['head']
		body = data['body']
		leg = data['leg'][monster.leg.direction]

		current_column = index % data['dimensions'][0]
		current_row = int(index / data['dimensions'][0])

		coord_left_top_x = padding + (current_column * (monster_width + gap))
		coord_left_top_y = padding + (current_row * (monster_height + gap))
		coord_right_bot_x = coord_left_top_x + monster_width
		coord_right_bot_y = coord_left_top_y + monster_height
		
		index += 1
		monster_draw.rectangle([coord_left_top_x, coord_left_top_y, coord_right_bot_x, coord_right_bot_y], fill=None, outline='black')

	monster_image.show()
if __name__ == '__main__':
	main()
