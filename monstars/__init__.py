#!/usr/bin/env python3

import random
import json
from PIL import Image, ImageDraw
import math

from classes import utilities as util 
from classes import images as img
from classes.properties import Attributes, Sizes
from classes.monster import Monster

def main():
	#read and store json file data
	data = util.reader()

	#store properties
	a = Attributes(data)
	s = Sizes(data)
	#create given number of monster objects: int, int
	monsters = util.create_monsters(a.columns, a.rows)

	#assign a name to each monster
	names = util.get_names(a)

	#create image
	monster_image = Image.new('RGB', (math.ceil(a.image_width), math.ceil(a.image_height)), util.hsl(100, 50, 50))
	monster_draw = ImageDraw.Draw(monster_image) # put this in image module
	
	#draw monsters
	for index, monster in enumerate(monsters, start=0):
		# base variables
		ox = (a.padding + (index % a.columns * (a.monster_width + a.gap)) )
		oy = (a.padding + (int(index / a.columns) * (a.monster_height + a.gap)))
		color = util.random_color()
		
		#body
		monster_draw = img.get_body(ox, oy, s, a, monster_draw) 
		
		#head
		monster_draw = img.get_head(ox, oy, s, a, monster, monster_draw, color)
		
		#arms
		monster_draw = img.get_left_arm(ox, oy, s, a, monster, monster_draw, color)
		monster_draw = img.get_right_arm(ox, oy, s, a, monster, monster_draw, color)
		
		#legs
		monster_draw = img.get_legs(ox, oy, s, a, monster, monster_draw, color)
		#name
		monster_draw = img.get_name(ox,oy,s,a,monster_draw, names, index)

		#display image
	monster_image.show()

if __name__ == '__main__':
	main()

#TODO háttér-figura eltérés, arc, minta, background, csápok
