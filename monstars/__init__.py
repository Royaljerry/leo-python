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
	monster_image.show()
	print(monsters)

if __name__ == '__main__':
	main()
