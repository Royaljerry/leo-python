#!/usr/bin/env python3

from car import Car

def main():
	my_first_car = Car('maserati', 'jsdhjdfhg')
	print(my_first_car.get_number_of_doors())
	print(my_first_car.car_color)
	print(my_first_car.addXToName())

if __name__ == '__main__':
	main()
