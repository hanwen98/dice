import random
import specialInputModule

side = specialInputModule.int_input("How many sides should the die have?")
dice_number = specialInputModule.int_input("How many dice do you want to roll?")

for time in range(1,dice_number+1):
	dice = random.randint(0,side)
	print "The result is %d" %(dice)

# 