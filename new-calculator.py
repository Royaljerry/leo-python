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
	# while… (number vagy =)
	# while (operator)
	current_input = input('Type the next item: ')
	USER_INPUT.append(current_input)

print(len(USER_INPUT) % 2)

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
