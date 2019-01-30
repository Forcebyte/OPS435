#!/usr/bin/env python3

#sys used to take the arguments for the script
import sys

#import the first and second argument as variables
firstarg = int(sys.argv[1])
secondarg = str(sys.argv[2])

#test to ensure that the number of times to loop isn't 0 or negative
if firstarg <= 0:
	print("ValueError: the first argument must be greater than 0.")
	exit()

#Create a while loop to loop through the command n amount of times
while firstarg != 0:
	print(secondarg)
	firstarg = firstarg - 1
