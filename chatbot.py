#!/usr/bin/env python3

import datetime, sys

CURRENT_HOUR = datetime.datetime.now().hour
YOUNG_AGE = 18
user_age = ''
greeting = ''
gender = ''

DAYTIME = {
	'morning' : (5, 6, 7, 8, 9, 10, 11),
	'afternoon' : (12, 13, 14, 15, 16),
	'evening' : (17, 18, 19, 20, 21),
	'night' : (22, 23, 24, 0, 1, 2, 3, 4),
}

USERS = {
	'male': (
		'Mr. ',
		(
			'Leó',
			'Ádám',
			'Dani',
			'Attila',
			'Marcell'
		)
	),
	'female': (
		'Ms. ',
		(
			'Orsi',
			'Julianna',
			'Ági',
			'Liza',
			'Kati',
			'Dorka'
		)
	)
}


def gender_check(user_name):
		if (user_name in USERS['male'][1]):
			return 'Mr. '
		elif (user_name in USERS['female'][1]):
			return 'Ms. '	

def greeting_abbr_string(string):
	return(string + ' wow!')

user_name = input("Hi, my name is Chatbot, what is your name? \n")

while not(str.isdigit(user_age) and (int(user_age) < 120)):
	user_age = input(user_name + ", how old are you? \n")

if (int(user_age) < YOUNG_AGE):
	greeting += 'Hello ' + str(user_name)
else:
	if (user_name in USERS['male'][1]):
		greeting_abbr = greeting_abbr_string(USERS['male'][0])
	elif (user_name in USERS['female'][1]):
		greeting_abbr = greeting_abbr_string(USERS['female'][0])
	else:
		while not(gender in USERS.keys()):
			gender = input("What is your sex? (male/female)")
		greeting_abbr = USERS[gender][0]
	for index in DAYTIME:
		if (CURRENT_HOUR in DAYTIME[index]):
			greeting += 'Good ' + index + ' ' + greeting_abbr + str(user_name)

print(greeting)
