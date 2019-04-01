#!/usr/bin/env python3
'''
   authorship declaration

   __author__ Patrick Turney
   __date__ March 2018
   __version__ 0.5
 
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
from time import strftime

def get_login_rec(login_recs,args):
	'''
	get_login_rec(login_recs,args) -> hosts/users
		takes a login list, along with a single (or list of ) argument(s)
		returns a list of users, or hosts with that record, depending on the argument
	
		e.g. get_login_rec(hosts,(192.168.1.1,192.168.1.2,192.168.1.2)) -> ["192.168.1.1","192.168.1.2"]
				get_login_rec(usersdsksjgkjk,("john,paul,ron,paul,stephan")) -> ["john", "paul", "ron", "stephan"]
	'''
	#Grab every Argument given to the function, either user (wants the users logged in) or host (wants the host IP)
	argument = str(args.list)
	#If the argument is asking for the user list, run through and give each line that contains that unique user
	if "user" in argument:
		users = []
		for item in login_recs:
			split = item.split()
			user = split[0]
			if user not in users:
				users.append(user)
		#Return a list of unique users
		return(users)
	#If the argument is asking for the host list, run through and give each unique host
	if "host" in argument:
		hosts = []
		for item in login_recs:
			split = item.split()
			host = split[2]
			if host not in hosts:
				hosts.append(host)
		#Return a list of unique hosts
		return(hosts)

def read_login_rec(filelist,args):
	'''
	read_login_rec(fielist,args) -> Array_Of_ImportantLines
		takes a list of files, along with a single (or list of ) argument(s)
		returns each line of each file in which that the user (or host) is mentioned

		e.g. read_login_rec(file.txt,argslist) -> Important lines for file.txt
				read_login_rec([file.txt,file2.txt],argslist) -> Important lines for both file.txt and flle2.txt
	'''
	if isinstance(filelist, str):
		filelist = [filelist]
	if (args.verbose is True) and (args.user is not None):
		print("Usage Report for User: " + str(args.user))
		print("Usage Report Type " + str(args.type[0]))
		print("processing usage report for the following: ")
		print("reading login/logout record files: " + str(filelist))
	elif (args.verbose is True) and (args.rhost is not None):
		print("Usage Report for Remote Host: " + str(args.rhost))
		print("Usage Report Type " + str(args.type[0]))
		print("processing usage report for the following: ")
		print("reading login/logout record files: " + str(filelist))
	elif (args.verbose is True and args.list):
		print("reading login/logout record files: " + str(filelist))
		print("processing usage report for the following: ")

	#Takes each record from filelist, adds it to a list
	unfiltered = []
	#Read the record
	for fileitem in filelist:
			file = open(fileitem,"r")
			unfiltered.extend(file.read().splitlines())

	#If there is an rhost argument (filter by IP), we filter by IP and add it to filtered
	#If there isn't just set filtered to be unfiltered for future filtering
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

def betweendays(split):
	'''
	
	'''
	dictmonth = {"Jan":"1", "Feb":"2","Mar":"3","Apr":"4","May":"5","Jun":"6","Jul":"7","Aug":"8","Sep":"9","Oct":"10","Nov":"11","Dec":"12"}	
	#Get both the starting and ending date
	startdate_obj = time.strptime(str((' '.join(split[3:8]))))
	enddate_obj = time.strptime(str((' '.join(split[9:14]))))

	#Get midnight of the ending date's day (midnight of next day)
	nextday = strftime('%d %m %y',enddate_obj)
	nextday = time.strptime(nextday, '%d %m %y')

	#################################################
	#Previous day time difference calculations
	#Get time difference between for the previous day
	prvday_timediff = int(time.mktime(nextday) - time.mktime(startdate_obj))
	#################################################
	#Next day time difference calculations
	#	Get time difference for the next day (12:00 - nxtday)
	nxtday_timediff = int((time.mktime(enddate_obj) - (time.mktime(nextday))))
	return(prvday_timediff,nxtday_timediff)

def cal_daily_usage(login_recs, args):
	'''
	cal_daily_usage(login_recs) -> timedict
		takes the login record lines generated in read_login_rec, and calculates the daily usage of each user or host mentioned
		finally, it returns a dictionary with each day, and the total time for that day
		Note that this function depends on parse_time, as it calculates time's down to the second for outputting

		e.g. cal_daily_usage(login_recs) -> Dictionary of time totals
	'''
	#If we're running verbosely, run with arguments for each file
	timedict = {}
	for item in login_recs:
		#Split item into catagories
		split = item.split()

		#Turns date into format similar to "Dec 30 23:38:51 2017"
		startdate_obj = time.strptime(str((' '.join(split[3:8]))))
		enddate_obj = time.strptime(str((' '.join(split[9:14]))))

		#Generate a date object to use in the dictionary we will check against and later add to
		dictmonth = {"Jan":"1", "Feb":"2","Mar":"3","Apr":"4","May":"5","Jun":"6","Jul":"7","Aug":"8","Sep":"9","Oct":"10","Nov":"11","Dec":"12"}	

		startdate_dy = strftime("%d", startdate_obj)
		enddate_dy = strftime("%d", enddate_obj)

		#If the entry is not on the same day, we take the median date between the two
		#After taking the median day, startdate usage is equal to the median day minus the startdate
		#Likewise, the ending day is just equal to the ending time...
		if  startdate_dy != enddate_dy:
			timedifferences = betweendays(split)
			prvday = str(split[7]) + " " + dictmonth.get(str(split[4])) + " " + str(split[5])	

			if prvday in timedict:
				newtime = int(timedict[prvday]) + int(timedifferences[0]) - 2
				timedict[prvday] = newtime
			else:
				timedict[prvday] = int(timedifferences[0])

			nxtday = str(split[13]) + " " + dictmonth.get(str(split[10])) + " " + str(split[11])
			if nxtday in timedict:
				newtime = int(timedict[nxtday]) + int(timedifferences[1])
				timedict[nxtday] = newtime
			else:
				timedict[nxtday] = int(timedifferences[1])
		else:
			month = str(split[4])
			month = dictmonth.get(month)
			dateobject = str(split[7]) + " " + month + " " + str(split[5])

			#Get the difference between those dates, and store it to timediff
			timediff = str(int((time.mktime(enddate_obj) - time.mktime(startdate_obj))))
			#If entry is in our time dictionary, add it to the date mentioned
			#If not, create a new entry
			if dateobject in timedict:
				oldtime = timedict[dateobject]
				newtime = int(timediff) + int(oldtime)
				timedict[dateobject] = newtime
			else:
				timedict[dateobject] = str(timediff)
	return(timedict)


def cal_weekly_usage(login_recs,args):
	'''
	cal_weekly_usage(login_recs) -> timedict
		takes the login record lines generated in read_logientryn_rec, and calculates the weekly usage of user or host mentioned
		finally, it returns a dictionary with each week, and the total time for that week
		Note that this function depends on parse_time, as it calculates time's down to the second for outputting

		e.g. cal_weekly_usage(login_recs) -> Dictionary of time totals
	'''
	timedict = {}

	#If we're running verbosely, run with arguments for each file
	if (args.verbose is True) and (args.user is not None):
		print("Usage Report for User: " + str(args.user))
		print("Usage Report Type " + str(args.type[0]))
		print("processing usage report for the following: ")
	elif (args.verbose is True) and (args.rhost is not None):
		print("Usage Report for Remote Host: " + str(args.rhost))
		print("Usage Report Type " + str(args.type[0]))
		print("processing usage report for the following: ")

	if (args.verbose is True):
			print("reading login/logout record files: [" + str(args.type[1])+ "]")

	for item in login_recs:
		#Split item into catagories
		split = item.split()


		#Convert both of those dates to time objects
		startdate_obj = time.strptime(str((' '.join(split[3:8]))))
		enddate_obj = time.strptime(str((' '.join(split[9:14]))))

		#Grab a week number from each entry to compare
		startdate_wk = strftime("%W", startdate_obj)
		enddate_wk = strftime("%W", enddate_obj)

		#Grab a day number from each entry to compare
		startdate_dy = strftime("%d", startdate_obj)
		enddate_dy = strftime("%d", enddate_obj)
		timeholders = 0
		if startdate_dy != enddate_dy:
			timeholders = 1
			timedifferences = betweendays(split)
			if startdate_wk != enddate_wk:
				prvweek = str(split[13]) + " " + str(startdate_wk)
				if prvweek in timedict:
					newtime = int(timedict[prvweek]) + int(timedifferences[0]) - 2
					timedict[prvweek] = newtime
				else:
					timedict[prvweek] = int(timedifferences[0])
				nxtwk = str(split[13]) + " " + str(enddate_wk)
				if nxtwk in timedict:
					newtime = int(timedict[nxtwk]) + int(timedifferences[1])
					timedict[nxtwk] = newtime
				else:
					timedict[nxtwk] = int(timedifferences[1])
		dateobject = str(split[13]) + " " + str(startdate_wk)
		timediff = int(time.mktime(enddate_obj) - time.mktime(startdate_obj)) 
		if dateobject in timedict:
			newtime = timediff + timedict[dateobject] - timeholders
			timedict[dateobject] = newtime
		else:
			timedict[dateobject] = timediff
	return(timedict)

def cal_monthly_usage(login_recs, args):
	#If we're running verbosely, run with arguments for each file
	if (args.verbose is True) and (args.user is not None):
		print("Usage Report for User: " + str(args.user))
		print("Usage Report Type " + str(args.type[0]))
		print("processing usage report for the following: ")
	elif (args.verbose is True) and (args.rhost is not None):
		print("Usage Report for Remote Host: " + str(args.rhost))
		print("Usage Report Type " + str(args.type[0]))
		print("processing usage report for the following: ")

	timedict = {}
	if (args.verbose is True):
		print("reading login/logout record files: [" + str(args.type[1])+ "]")
	for item in login_recs:
		#Split item into catagories
		split = item.split()

		#generate a month object that we will check against later
		dictmonth = {"Jan":"1", "Feb":"2","Mar":"3","Apr":"4","May":"5","Jun":"6","Jul":"7","Aug":"8","Sep":"9","Oct":"10","Nov":"11","Dec":"12"}

		#Convert both dates into time objects
		startdate_obj = time.strptime(str((' '.join(split[3:8]))))
		enddate_obj = time.strptime(str((' '.join(split[9:14]))))

		#Grab a day number from each entry to compare
		startdate_dy = strftime("%d", startdate_obj)
		enddate_dy = strftime("%d", enddate_obj)
		startdate_mn = strftime("%m", startdate_obj)
		enddate_mn = strftime("%m", enddate_obj)
		timeholders = 0
		if startdate_dy != enddate_dy:
			timeholders = 1
			timedifferences = betweendays(split)
			if startdate_mn != enddate_mn:
				prvmonth = str(split[7]) + " " + startdate_mn
				if prvmonth in timedict:
					newtime = int(timedict[prvmonth]) + int(timedifferences[0]) - 2
					timedict[prvweek] = newtime
				else:
					timedict[prvweek] = int(timedifferences[0])
				nxtmonth = str(split[13]) + " " + enddate_mn
				if nxtmonth in timedict:
					newtime = int(timedict[nxtmonth]) + int(timedifferences[1])
					timedict[nxtmonth] = newtime
				else:
					timedict[nxtmonth] = int(timedifferences[1])
				break
		dateobject = str(split[13]) + " " + enddate_mn
		timediff = int(time.mktime(enddate_obj) - time.mktime(startdate_obj))
		if dateobject in timedict:
			newtime = timediff + timedict[dateobject] - timeholders
			timedict[dateobject] = newtime
		else:
			timedict[dateobject] = timediff
	return(timedict)

def print_statement(dictionary,usertype,subject):
	line = str(usertype) + "ly Usage Report for " + str(subject)
	eq = len(line)
	print(line)
	print ("=" * eq)  
	if str(usertype) == "Dai":
		print("%-15s %-15s" %("Date","Usage in Seconds"))
	if str(usertype) == "Weekly":
		print("%-15s %-15s" %("Week #","Usage in Seconds"))
	if str(usertype) == "Month":
		print("%-15s %-15s" %("Month","Usage in Seconds"))

	total = 0
	for key, value in sorted(dictionary.items(),reverse=True):
		print("%-10s %-10s" %(str(key),"    " + str(value)))
		total = total + int(value)
	print("%-10s %-10s" %("Total","    " + str(total)))

if __name__ == '__main__':
	import argparse
	#Initialize all arguments to parse in main
	parser = argparse.ArgumentParser()
	parser.add_argument("-F", "--file", help="list of files to be processed")
	parser.add_argument("-l", "--list",  help="generate user name or remote host IP from the given files", nargs=2)
	parser.add_argument("-r", "--rhost",  help="usage report for the given remote host IP")
	parser.add_argument("-t", "--type",  help="type of report: daily, weekly, and monthly", nargs=2)
	parser.add_argument("-u", "--user", help="usage report for the given user name")
	parser.add_argument("-v", "--verbose", help="turn on output verbosity", action="store_true")
	#[ code to retrieve command line argument using the argparse module 
	args = parser.parse_args()

	#Run if arguments exist
	if args is not None:
		#If we're running verbosely, run with arguments for each file
		#If running with -l (E.g. ./ur.py -l user/host test.txt)
		if args.list is not None:
			#Since we are running with -l, the file that we are using is specified in the fourth argument
			subject = str(sys.argv[2])
			args.file = [str(sys.argv[3])]
			if args.verbose is True:
				print("Files to be processed " + str(args.list[1]))
				print("Types of args for files <class 'list'>")
			login_rec = read_login_rec(args.file,args)
			userhost_rec = get_login_rec(login_rec,args)
			userhost_rec.sort()
			if args.verbose is True:
				print("Generating list for " + subject)
			item = (str(args.list[0])).capitalize()
			line = str(item) + " list for " + str(args.list[1])
			eq = len(line)
			print(line)
			print("=" * eq)

			#Now that we are done, print the user or host involved by passing through each host/user in the list
			for user_or_host in userhost_rec:
				print(user_or_host)
		
		#If running with -r (E.g. ./ur.py -r 10.0.0.1 test.txt)
		if args.rhost or args.user is not None:
			if args.verbose is True:
				placeholder = []
				placeholder.append(str(sys.argv[5]))
				print("Files to be processed " + str(placeholder))
				print("Types of args for files " + str(type(placeholder)))
			#Grab the bulk file, and parse it
			args.file = [str(sys.argv[5])]
			login_rec = read_login_rec(args.file,args)
			
			#In this case, the timeframe will be what the user wants
			timeframe = str(sys.argv[4])


			subject = str(sys.argv[2])

			#If asking for a daily report (E.g. ./ur.py -r 10.0.0.1 daily test.txt)
			if "daily" in timeframe:
				#Grab the ditionary for daily usage
				daily_dict 	= cal_daily_usage(login_rec,args)
				print_statement(daily_dict,"Dai",subject)


			#If asking for a weekly report (E.g. ./ur.py -r 10.0.0.1 weekly test.txt)
			if "weekly" in timeframe:
				weekly_dict = cal_weekly_usage(login_rec,args)
				print_statement(weekly_dict,"Week",subject)


			#If asking for a monthly report (E.g. ./ur.py -r 10.0.0.1 monthly test.txt)
			if "monthly" in timeframe:
				monthly_dict = cal_monthly_usage(login_rec,args)
				print_statement(monthly_dict,"Month",subject)
else:
	parser.print_help()
class parser(argparse.ArgumentParser):
	def error(self, message):
		sys.stderr.write('error: %s\n' % message)
		parser.print_help()
		sys.exit(2)		