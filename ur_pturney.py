#!/usr/bin/env python3
'''
   authorship declaration

   __author__ Patrick Turney
   __date__ March 2018
   __version__ 0.1
 
   OPS435 Assignment 2 - Fall 2018
	Program: ur_pturney.py
	Author: "Patrick Turney"
	The python code in this file ur_pturney.py is original work written by
	"Patrick Turney". No code in this file is copied from any other source 
	including any person, textbook, or on-line resource except those provided
	by the course instructor. I have not shared this python file with anyone
	or anything except for submission for grading.  
	I understand that the Academic Honesty Policy will be enforced and violators 
	will be reported and appropriate action will be taken.
'''

import os 
import sys
import time

#def get_login_rec():
	''' docstring for this fucntion
	get records from the last command
	filter out the unwanted records
	add filtered record to list (login_recs)'''
	#[ put your python code for this function here ]
	#return login_recs
 
def read_login_rec(filelist,args):
	''' docstring for this function
	get records from given filelist
	open and read each file from the filelist
	filter out the unwanted records
	add filtered record to list (login_recs)''' 
	#[ put your python code for this function here ]

	#Takes each record from filelist, adds it to a list
	unfiltered = []
	for fileitem in filelist:
		file = open(fileitem,"r")
		unfiltered.append(file.readlines())
	print(unfiltered)
	#If there is an rhost argument (filter by IP), we filter by IP and add it to filtered
	# If there isn't just set filtered to be unfiltered for future filtering
	filtered = []
	if args.rhost is not None:
		for item in unfiltered:
			if str(args.rhost) in item:
				filtered.append(item)
	else:
		filtered = unfiltered

	#If there is a user argument (filter by username), we filter by the username and add it
	#To the filteredfinal list, if there isn't, just set filtered to be filteredfinal and return
	filteredfinal = []
	if args.user is not None:
		for item in filtered:
			if str(args.user) in item:
				filteredfinal.append(item)
	else:
		filteredfinal = filtered
	login_rec = filteredfinal
	return login_rec

#def cal_daily_usage(subject,login_recs):
	''' docstring for this function
	generate daily usage report for the given 
	subject (user or remote host)'''
	#[ put your python code for this function here ]
	#return daily_usage

#def cal_weekly_usage(subject,login_recs):
	''' docstring for this function
	generate weekly usage report for the given 
	subject (user or remote host)'''
	#[ put your python code for this function here ]
	#return weekly_usage

#def cal_monthly_usage(subject,login_recs):
	''' docstring for this function
	generate monthly usage report fro the given
	subject (user or remote host)'''
	#[ put your python code for this function here ]
	#return monthly_usage
	 
if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("-F", "--file", help="list of files to be processed", required=True)
	parser.add_argument("-l", "--list",  help="generate user name or remote host IP from the given files")
	parser.add_argument("-r", "--rhost",  help="usage report for the given remote host IP")
	parser.add_argument("-t", "--type",  help="type of report: daily, weekly, and monthly")
	parser.add_argument("-u", "--user", help="usage report for the given user name")
	parser.add_argument("-v", "--verbose", help="turn on output verbosity")
	#[ code to retrieve command line argument using the argparse module [
	args = parser.parse_args()

	if args.user is not None:
		args.file = [args.file]
		login_rec = read_login_rec(args.file,args)
		print(login_rec)
	#[ based on the command line option, generate and print
	#  the requested usage report ]
