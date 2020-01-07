#!/Users/adam.pocs/.pyenv/shims/python

import json
from classes.monster import Monster

data = ''

if __name__ == '__main__':
	print('monsters running')
	with open("data/data.json", "r") as read_file:
		data = json.load(read_file)
		read_file.close()
	print(data)
	my_monster = Monster()