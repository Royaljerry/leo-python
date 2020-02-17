import random

def reverseString(string):
	return string[::-1]


def hsl(h, s, l):
	r = ""
	r += "hsl("
	r += str(h) + ", "
	r += str(s) + "%, "
	r += str(l) + "%"
	r += ")"
	return r

def get_direction():
	return(random.randint(0, 2))

def get_real_pixel(dimensions, monster_pixels):
	real_pixel = []
	real_pixel.append(monster_pixels[0] / dimensions[0])
	real_pixel.append(monster_pixels[1] / dimensions[1])
	return real_pixel

