#!/usr/bin/env python3

import json
from classes.monster import Monster

data = ''

def create_monsters(monsters_hor, monsters_ver):
	for row in range(monsters_ver):
		for column in range(monsters_hor):
			monster = Monster()

def main():
	with open("data/data.json", "r") as read_file:
		data = json.load(read_file)
		read_file.close()
	create_monsters(data['dimensions'][0], data['dimensions'][1])

if __name__ == '__main__':
	main()
