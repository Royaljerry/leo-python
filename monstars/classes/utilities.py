from PIL import Image, ImageDraw
import random
import json
from classes.monster import Monster
from classes.properties import Sizes, Attributes
def reader():
	props = {
		"arm": {
			"straight" : [],
			"downwards": [],
			"upwards" : []
			},
		"leg": {
			"front": [],
			"left": [],
			"right": []
			}
		}
	choice = input('1 : alapértelmezett beállítások\n2 : egyéni méretek ')
	while True:
		if choice == '1' or choice == '2':
			break
		else:
			choice = input('1 / 2 ')
	if choice == '1':
		alapertelmezett = "data/data.json"
		with open(alapertelmezett, "r") as f:
			data=json.load(f)
			f.close()
	elif choice == '2':
		try:
			with open('data/user_size.json', "w") as f:
				props["dimensions"] = splitter(input('dimensions: '))
				props["monster_size"] = splitter(input('monsters size: '))
				props["gap"] = splitter(input('margin: '))
				props["padding"] = splitter(input('padding: '))
				props["palm"] = splitter(input('palms: '))
				props["foot"] = splitter(input('feet: '))
				props["head"] = splitter(input('head: '))
				props["body"] = splitter(input('body: '))
				props["arm"]["straight"] = splitter(input('arm: '))
				props["arm"]["downwards"] = [props["arm"]["straight"][0] - props["palm"][0], props["arm"]["straight"][0] ]
				props["arm"]["upwards"] = props["arm"]["downwards"]
				props["leg"]["front"] = splitter(input("legs: "))
				props["leg"]["left"] = props["leg"]["front"][0], props["leg"]["front"][1] - props["foot"][1]
				props["leg"]["right"] = props["leg"]["left"]
				json.dump(props, f)
				f.close()
				with open("data/user_size.json", "r") as f:
					data = json.load(f)
					f.close()
		except:
			print('Hibás adatbevitel, újrakezdés...')
			reader()
	return data

def create_monsters(monsters_hor, monsters_ver):
	monsters = []
	for row in range(int(monsters_ver)):
		for column in range(int(monsters_hor)):
			monster = Monster()
			monsters.append(monster)
	return monsters

def hsl(h, s, l):
	r = ""
	r += "hsl("
	r += str(h) + ", "
	r += str(s) + "%, "
	r += str(l) + "%"
	r += ")"
	return r

def random_color():
	h = random.randint(0,360)
	s = random.randint(20,100)
	l = random.randint(15,80)
	return ("hsl({},{}%,{}%)".format(h,s,l))

def get_direction():
	return(random.randint(0, 2))

def get_real_pixel(dimensions, monster_pixels):
	real_pixel = []
	real_pixel.append(monster_pixels[0] / dimensions[0])
	real_pixel.append(monster_pixels[1] / dimensions[1])
	return real_pixel

def splitter(inp):
    r = []
    if ',' in inp:
        s = ','
    else:
        s = ' '
    l = inp.split(s)
    for n in l:
        r.append(float(n))
    return r

def convert_x(x,a):
	x *a.ph
	return x
def convert_y(y,a):
	y *a.pv
	return y
def get_names(a):
	names = []
	with open('data/names.txt','r') as f:
			data = f.readlines()
			f.close()
	for line in data:
		line = line.strip()
		if random.randint(0,1) == 1: 
			names.append(line)
		if len(names) == a.rows * a.columns:
			break
	return names

