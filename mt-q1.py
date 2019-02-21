#!/usr/bin/env python3
'''Student Name: Patrick Turney
   Student ID: pturney
   Program: mt-q1.py '''

import sys

argumentlist = sys.argv[1::]

print("Number of numbers received: " + str(len(argumentlist)))
print("List of numbers received: " + str(argumentlist))

total = 0

for item in argumentlist:
	total = int(total) + int(item)
	

avg = total / len(argumentlist)
print("Average for the given numbers: " + str(avg))
