#!/usr/bin/env python3

from car import Car

def main():
	my_first_car = Car('ymdbdfb', 'red', 'bmw')
	print(my_first_car.get_number_of_doors())

if __name__ == '__main__':
	main()
