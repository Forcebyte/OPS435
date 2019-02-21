#!/usr/bin/env python3

import sys

answer = "0"

while answer != "1":
	number1 = input("Please Enter the first number: ")
	number2 = input("Please enter the second numbeer: ")

	if(int(number1)%int(number2) == 0):
		print(str(number1) + " is divisable by " + str(number2) + ". Thanks!")
		answer = "1"
	else:
		print(str(number1) + " is not divisible by " + str(number2) + ". Please try again.")
