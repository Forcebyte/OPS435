#!/usr/bin/env python3

import sys

def get_mark():
	mark = input("Please enter a mark (0-100): ")
	return(mark)

def mark_2_grade(marknum):
	marknum = int(marknum)
	if(marknum >= 90):
		grade = "A"
		return(grade)
	elif(marknum >= 80):
		grade = "B"
		return(grade)
	elif(marknum >= 70):
		grade = "C"
		return(grade)
	elif(marknum >= 60):
		grade = "D"
		return(grade)
	else:
		grade = "F"
		return(grade)

marknum = get_mark()
grade = mark_2_grade(marknum)
print("Your Grade is " + grade + ".")
