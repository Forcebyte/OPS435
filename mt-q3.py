#!/usr/bin/env python3
'''Student Name: Patrick Turney
   Student ID: pturney
   Program: mt-q3.py '''

def gpv(userinput):
	userinput = userinput.split(' ')
	gpatotal = []
	for item in userinput:
		if(item == "A"):
			gpatotal.append("4")
		elif(item == "B"):
			gpatotal.append("3")
		elif(item == "C"):
			gpatotal.append("2")
		elif(item == "D"):
			gpatotal.append("1")
		else:
			gpatotal.append("0")
	return(gpatotal)

def cal_gpa(listgpa):
	totalcount = len(listgpa)
	total = 0
	for item in listgpa:
		total = total  + int(item)
	gpa = int(total) / int(totalcount)
	return(gpa)
if __name__ == '__main__':
	userinput = input("Please enter a list of grades: ")
	listgpa = gpv(userinput)
	GPA = cal_gpa(listgpa)
	GPA = int(GPA)
	print("Your GPA is " + str(GPA) + ".")
