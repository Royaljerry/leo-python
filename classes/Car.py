#!/usr/bin/env python3

import json

class Car:
	def __init__(self, car_name, car_color, car_type):
		self.car_name = car_name
		self.car_color = car_color
		self.car_type = car_type
		with open("settings.json", "r") as read_file:
			self.CAR_TYPES = json.load(read_file)
		read_file.close()
		# print(self.CAR_TYPES)

	def go(self, distance):
		return(self.car_name + '.'*distance)

	def get_number_of_doors(self):
		car_type = self.car_type
		if (car_type in self.CAR_TYPES["items"]):
			number_of_doors = self.CAR_TYPES["items"]["doors"][""]
			return number_of_doors
		else: 
			return 'Unknown car type'

		
my_first_car = Car('kispiros', 'red', 'bmw')
# print(my_first_car.go(5))
print(my_first_car.get_number_of_doors())

# todo: python server install on local machine
# next steps: argument list, getter, setter methods, json import
