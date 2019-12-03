#!/usr/bin/env python3

import json

class Car:
	def __init__(self, car_name, car_color):
		self.car_name = car_name
		with open("settings.json", "r") as read_file: self.CARS = json.load(read_file)
		read_file.close()
		if (car_color in self.CARS[car_name]["color"]):
			self.car_color = car_color
		else:
			self.car_color = "default"
	

	def go(self, distance):
		return(self.car_name + '.'*distance)

	def addXToName(self):
		return(car_name + 'X')

	def get_number_of_doors(self):
		car_name = self.car_name
		if (car_name in self.CARS):
			number_of_doors = self.CARS[car_name]["doors"]
			return number_of_doors
		else:
			return 'Unknown car type'

# todo: python server install on local machine
# next steps: argument list, getter, setter methods

if __name__ == '__main__':
	print('nothing here…')

