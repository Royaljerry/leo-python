#!/usr/bin/env python3

from .Car import Car

my_first_car = Car()

print(my_first_car)

my_first_car = Car('red', 'audi')
my_second_car = Car('green', 'bmw')

print(my_first_car.car_color)
print(my_first_car.car_type)
print(my_second_car.car_color)
print(my_second_car.car_type)
