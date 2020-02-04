#!/usr/bin/env python3

import json
from PIL import Image, ImageDraw

from classes import utilities
from classes.monster import Monster

# monsterImage = Image.new('RGB', (200, 200), utilities.hsl(100, 50, 50))
# monsterDraw = ImageDraw.Draw(monsterImage)
# monsterImage.show()

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

if __name__ == '__main__':
	main()
