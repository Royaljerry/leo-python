#!/usr/bin/env python3

number = ''
numbers = []
operations = []
while not (number == str('=')):     
    number += input('give items') 
    if (str.isdigit(number)):
        numbers.append(number)
    else:
       operations.append(number)

print (numbers) 