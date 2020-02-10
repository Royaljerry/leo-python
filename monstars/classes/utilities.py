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
