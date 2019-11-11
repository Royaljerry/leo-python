#!/usr/bin/env python3

import json

class Car:
	def __init__(self, car_name, car_color, car_type):
		self.car_name = car_name
		self.car_color = car_color
		self.car_type = car_type
		with open("settings.json", "r") as read_file: self.CARS = json.load(read_file)
		read_file.close()

	def go(self, distance):
		return(self.car_name + '.'*distance)

	def get_number_of_doors(self):
		car_name = self.car_name
		# in_cars = any(x["name"] == car_type for x in self.CARS["items"])
		if (car_name in self.CARS):
			number_of_doors = self.CARS[car_name]["doors"]
			return number_of_doors
		else:
			return 'Unknown car type'

# todo: python server install on local machine
# next steps: argument list, getter, setter methods

if __name__ == '__main__':
	print('nothing here…')

