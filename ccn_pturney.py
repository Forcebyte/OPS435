#!/usr/bin/env python3
'''
   authorship declaration

   __author__ Patrick Turney
   __date__ March 2019
   __version__ 1.0
 
 OPS435 Assignment 3 - Fall 2018
Program: ccn_pturney.py
Author: Patrick Turney
The python code in this file ccn_pturney.py is original work written by
Patrick Turney. No code in this file is copied from any other source 
including any person, textbook, or on-line resource except those provided
by the course instructor. I have not shared this python file with anyone
or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and violators 
will be reported and appropriate action will be taken.
   
'''
import os
import sys
import time




if __name__ == '__main__':
    import argparse
	#Initialize all arguments to parse in main
	parser = argparse.ArgumentParser()
	parser.add_argument("-N", "--notify", help="list of notification subscription sites to be processed")
	parser.add_argument("-s", "--site",  help="class cancellation web site")
	parser.add_argument("-t", "--type {table,text}",  help="type of class cancellation data: table -> html table,\ntext -> plain text file")
	parser.add_argument("-n", "--table {table,text}",  help="type of notification data: table -> html table, text \nplain text file")
	#retrieve command line arguments using the argparse module 
	args = parser.parse_args()
