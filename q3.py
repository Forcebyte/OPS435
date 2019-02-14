#!/usr/bin/env python3

import sys

arg1 = sys.argv[1]

if (len(arg1) == 1):
	print("Sorry, " + str(arg1) + " has only " + str(len(arg1)) + " letter.")
	print("Please give me a nine-letter word.")
elif (len(arg1) != 9):
	print("Sorry, " + str(arg1) + " has only " + str(len(arg1)) + " letters.")
	print("Please give me a nine-letter word.")
else:
	strarg1 = str(arg1)
	entercde = strarg1[0] + strarg1[2] + strarg1[4] + strarg1[6] + strarg1[8]
	extcde = strarg1[8] + strarg1[6] + strarg1[4] + strarg1[2] + strarg1[0]
	
	print("Thank you for your cooperation.")
	print("Here is the enter code: " + entercde)
	print("And the exit code is: " + extcde)
