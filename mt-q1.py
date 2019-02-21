#!/usr/bin/env python3

import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
total = num1 * num2

answer = input("Please enter how much is " + str(num1) + " * " + str(num2) + ": ")
if (str(total) == str(answer)):
	print("You're Correct!")
else:
	print("Sorry! It's wrong. Correct Answer is " + str(num1*num2) + ".")

