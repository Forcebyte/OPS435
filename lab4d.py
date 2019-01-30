#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(string1):
    # Place code here - refer to function specifics in section below
	firstfive = string1[0:5]
	return(firstfive)

def last_seven(string1):
    # Place code here - refer to function specifics in section below
	lastseven = string1[-7:]
	return(lastseven)
def middle_number(number1):
    # Place code here - refer to function specifics in section below
	stringy = str(number1)
	secondthird = stringy[1:3]
	return(secondthird)
def first_three_last_three(str1,str2):
    # Place code here - refer to function specifics in section below
	firstthree = str1[0:3]
	lastthree =  str2[-3:]
	combined = firstthree + lastthree
	return(combined)
if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
