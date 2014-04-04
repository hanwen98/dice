#! /usr/bin/env python
import random
import specialInputModule

side = specialInputModule.int_input("How many sides should the die have?")
while side <= 1:
	print "That number is not valid."
	side = specialInputModule.int_input("How many sides should the die have?")

dice_number = specialInputModule.int_input("How many dice do you want to roll?")
while dice_number <= 0:
	print "That number is not valid."
	dice_number = specialInputModule.int_input("How many dice do you want to roll?")

for time in range(1,dice_number+1):
	dice = random.randint(1,side)
	print "The result is %d" %(dice)

# 