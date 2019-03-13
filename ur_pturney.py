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

def get_login_rec(login_recs,args):
	''' docstring for this fucntion
	get records from the last command
	filter out the unwanted records
	add filtered record to list (login_recs)'''
	#[ put your python code for this function here ]
	#return login_recs

	#Grab the Argument given, either user (wants the users logged in) or host (wants the host IP)
	argument = str(args.list)


	#Remove extra spaces from what we're dealing with. Unspaced becomes a filtered thing to grab from
	unspaced = []
	for item in login_recs:
		while '  ' in item:
			item = item.replace('  ',' ')
			unspaced.append(item)

	#If the argument is asking for the user list, run through and give users
	if "user" in argument:
		users = []
		#Grab each user for each line
		for item in unspaced:
			#split on each column, then grab first column
			split = item.split()
			user = split[0]
			#If it is unique, add it to users
			if user not in users:
				users.append(user)
		return(users)
	
	#If the argument is asking for the host list, run through and give hosts
	if "host" in argument:
		hosts = []
		for item in unspaced:
			split = item.split()
			host = split[3]
			#If it is unique, add it to hosts
			if item not in host:
				hosts.append(item)
		return(hosts)


def read_login_rec(filelist,args):
	''' docstring for this function
	get records from given filelist
	open and read each file from the filelist
	filter out the unwanted records
	add filtered record to list (login_recs)'''
	#[ put your python code for this function here ]

	#If we're just given one file, add it to a single array
	if isinstance(filelist, str):
			filelist = [filelist]
	#Takes each record from filelist, adds it to a list
	unfiltered = []

	#Read the record
	for fileitem in filelist:
			file = open(fileitem,"r")
			unfiltered.extend(file.read().splitlines())

	#If there is an rhost argument (filter by IP), we filter by IP and add it to filtered
	# If there isn't just set filtered to be unfiltered for future filtering
	filtered = []
	if args.rhost is not None:
		rhost = str(args.rhost)
		for item in unfiltered:
				if rhost in item:
						filtered.append(item)
	else:
		filtered = unfiltered
	#If there is a user argument (filter by username), we filter by the username and add it
	#To the filteredfinal list, if there isn't, just set filtered to be filteredfinal and return
	filteredfinal = []
	if args.user is not None:
		username = str(args.user)
		for item in filtered:
				if username in item:
						filteredfinal.append(item)
	else:
			filteredfinal = filtered
	login_rec = filteredfinal
	return login_rec



def cal_daily_usage(subject,login_recs):
	''' docstring for this function
	generate daily usage report for the given 
	subject (user or remote host)'''
	#[ put your python code for this function here ]
	#return daily_usage

def cal_weekly_usage(subject,login_recs):
	''' docstring for this function
	generate weekly usage report for the given 
	subject (user or remote host)'''
	#[ put your python code for this function here ]
	#return weekly_usage

def cal_monthly_usage(subject,login_recs):
	''' docstring for this function
	generate monthly usage report fro the given
	subject (user or remote host)'''
	#[ put your python code for this function here ]
	#return monthly_usage
	 
if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("-F", "--file", help="list of files to be processed")
	parser.add_argument("-l", "--list",  help="generate user name or remote host IP from the given files", nargs=2)
	parser.add_argument("-r", "--rhost",  help="usage report for the given remote host IP")
	parser.add_argument("-t", "--type",  help="type of report: daily, weekly, and monthly")
	parser.add_argument("-u", "--user", help="usage report for the given user name")
	parser.add_argument("-v", "--verbose", help="turn on output verbosity")
	#[ code to retrieve command line argument using the argparse module [
	args = parser.parse_args()

	#If there are arguments
	if args is not None:
		#If running with -l (E.g. ./ur.py -l user/host test.txt)
		if args.list is not None:
			#Since we are running with -l, the file that we are using is specified in the fourth argument
			args.file = [str(sys.argv[3])]
			login_rec = read_login_rec(args.file,args)
			userhost_rec = get_login_rec(login_rec,args)
			#Now that we are done, print the user or host involved by passing through each host/user in the list
			for user_or_host in userhost_rec:
				print(user_or_host)
		#Test running with listing
		#If running with -t (E.g. ./ur.py -u rchan -t daily usage_data_file)
		if args.type is not None:
			args.file= [args.file]
			login_rec = read_login_rec(args.file,args)
	#[ based on the command line option, generate and print
	#  the requested usage report ]