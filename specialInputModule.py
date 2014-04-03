#! /usr/bin/env python


def name_input(input):
	name = raw_input(input)
	if len(name) > 10:
		print "that name is too long. I'll give you a nickname"
		name = name[0:10]
	return name
	

def int_input(input):
	while True:
		age = raw_input(input)
		try: 
			age = int(age)
			return age
		except:
			print "that is not a number. Please try again."
		
	
	

def float_input(input):
	while True :
		guess = raw_input(input)
		try: 
			guess = float(guess)
			return guess
		except:
			print "that is not a number. Please try again."
		