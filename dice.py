import random
import specialInputModule

dice_number = specialInputModule.int_input("How many dice do you want to roll?")

for time in range(1,dice_number+1):
	side = specialInputModule.int_input("How many sides should the die have?")
	dice = random.randint(1,side+1)
	print "The result is %d" %(dice)

# 