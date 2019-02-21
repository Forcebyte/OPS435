#!/usr/bin/env python3
'''Student Name: Patrick Turney
   Student ID: pturney
   Program: mt-q2.py '''
total = int(0)
userinput = input("Please enter a ten digit number: ")
try:
	usernum = int(userinput)
except:
	usernum = "Notaint"

if (isinstance(usernum,int) and len(userinput) == 10):
	userlist = list(userinput)
	for num in userlist:
		total = total + int(num)
	print("OK, the sum of the 10 digits of " + str(usernum) + " is " + str(total) + ". Thanks!")
elif (len(userinput) != 10):
	print(userinput + " is not a ten digits number. Please try again.")
else:
	print(userinput + " is not a number. Please ry again.")
