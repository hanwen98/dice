import random
import specialInputModule
dice = random.randint(1,6)
side = specialInputModule.int_input("How many sides should the die have?")
dice_number = specialInputModule.int_input("How many dice do you want to roll?")
print "The result is %d" %(dice)