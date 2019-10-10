#!/usr/bin/env python3

OPERATORS = [
	'+',
	'-',
	'*',
	'/'
]

INPUT_TYPES = [
	'number',
	'operator'
]

USER_INPUT = []

current_input = ''

while not(current_input == '='):

	current_input = input('Type the next item: ')
	
	if (len(USER_INPUT) % 2 == 0):
		while not(str.isdigit(current_input) or str(current_input) == '='):
			if (str.isdigit(current_input)):
				USER_INPUT.append(current_input)
	else:
		while (current_input in OPERATORS):
			USER_INPUT.append(current_input)

	print('current user input' + str(USER_INPUT) + "\n")

print(USER_INPUT)

# number = ''
# numbers = []
# operations = []
# while not (number == str('=')):     
# 	number += input('give items')
# 	print(number)
# 	if (str.isdigit(number)):
# 		numbers.append(number)
# 	else:
# 		operations.append(number)
# print (numbers)
