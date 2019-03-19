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
	#If we're just given one file, add it to a single array
	if isinstance(filelist, str):
			filelist = [filelist]

	#If we're running verbosely, run with arguments for each file
	if args.verbose is True:
		print("Files to be processed:" + str(filelist))
		print("Type of args for files " + str(type(filelist)))

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

def bwteendays(timedict, split, args):
	'''
	Take login record that is not on the same day, and add it to respective records
	'''
	dictmonth = {"Jan":"1", "Feb":"2","Mar":"3","Apr":"4","May":"5","Jun":"6","Jul":"7","Aug":"8","Sep":"9","Oct":"10","Nov":"11","Dec":"12"}	
	#Get both the starting and ending date
	startdate_obj = time.strptime(str((' '.join(split[3:8]))))
	enddate_obj = time.strptime(str((' '.join(split[9:14]))))

	#Get midnight of the ending date's day (midnight of next day)
	nextday = strftime('%d %m %y',enddate_obj)
	nextday = time.strptime(nextday, '%d %m %y')
	month = dictmonth.get(str(split[4]))
	#Get dateobject, depending on args
	timeframe = str(sys.argv[4])
	if timeframe == "daily":
		begdateobject = str(split[7]) + " " + month + " " + str(split[5])
		enddateobject = str(split[13]) + " " + month + " " + str(split[11])
	if timeframe == "weekly":
		startdate_wk = strftime("%W", startdate_obj)
		enddate_wk = strftime("%W", enddate_obj)
		begdateobject = str(split[13]) + " " + str(enddate_wk)
		enddateobject = str(split[13]) + " " + str(enddate_wk)
	if timeframe == "monthly":
		begdateobject = str(split[7]) + " " + month
		enddateobject = str(split[13]) + " " + month

	#################################################
	#Previous day time difference calculations
	#Get time difference between for the previous day
	prvday_timediff = (time.mktime(nextday) - time.mktime(startdate_obj))


	if begdateobject in timedict:
		oldtime = timedict[begdateobject]
		newtime = int(float(prvday_timediff)) + int(float(oldtime)) - 2
		timedict[begdateobject] = newtime
	else:
		timedict[begdateobject] = str(prvday_timediff)
	#################################################
	#Next day time difference calculations
	#	Get time difference for the next day (12:00 - nxtday)
	nxtday_timediff = (time.mktime(enddate_obj) - (time.mktime(nextday)))
	month = dictmonth.get(str(split[10]))
	if enddateobject in timedict:
		oldtime = timedict[enddateobject]
		newtime = int(float(prvday_timediff)) + int(float(oldtime))
		timedict[enddateobject] = newtime
	else:
		timedict[enddateobject] = int(float(nxtday_timediff))
	return(timedict)

def cal_daily_usage(login_recs, args):
	'''
	cal_daily_usage(login_recs) -> timedict
		takes the login record lines generated in read_login_rec, and calculates the daily usage of each user or host mentioned
		finally, it returns a dictionary with each day, and the total time for that day
		Note that this function depends on parse_time, as it calculates time's down to the second for outputting

		e.g. cal_daily_usage(login_recs) -> Dictionary of time totals
	'''
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
			timedict = bwteendays(timedict, split, args)
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

		#Grab a week number from each entry to compare (%U is week number from 0-51)
		startdate_wk = strftime("%W", startdate_obj)
		enddate_wk = strftime("%W", enddate_obj)

		#If the entry is not on the same week, we take the median date between the two
		#After taking the median day, startdate usage is equal to the median day minus the startdate
		#Likewise, the ending day is just equal to the ending time...
		if startdate_wk != enddate_wk:
			nextday = strftime("%d %m %Y",enddate_obj)
			nextday = time.strptime(nextday, '%d %m %Y')


			###############################################################################
			#Previous day (12:00 - XX:XX) time difference, take it and round it out
			prvday_timediff = (time.mktime(nextday) - time.mktime(startdate_obj))
			#In this case, dateobject will be the beginning section of our string

			dateobject = str(split[13])	+ " " + str(startdate_wk)
			if dateobject in timedict:
				oldtime = timedict[dateobject]
				newtime = int(prvday_timediff) + int(oldtime) - 2
				timedict[dateobject] = newtime
			else:
				timedict[dateobject] = str(prvday_timediff)
				print(timedict)

			#Date Object to compare to our dictionary
			dateobject = str(split[13]) + " " + str(enddate_wk)
			###############################################################################
			#Next Day (XX:XX - 12:00) Time Difference
			nxtday_timediff = (time.mktime(enddate_obj) - (time.mktime(nextday)))

			if dateobject in timedict:
				oldtime = timedict[dateobject]
				newtime = int(nxtday_timediff) + int(oldtime) - 2
				timedict[dateobject] = newtime
			else:
				timedict[dateobject] = str(nxtday_timediff)
		else:
			###############################################################################
			dateobject = str(split[13]) + " " + str(startdate_wk)
			dateobject = str(dateobject)
			print("Dateobject = " + dateobject)

			#Get the difference between those dates, and store it to timediff
			timediff = (time.mktime(enddate_obj) - time.mktime(startdate_obj))

			#If entry is in our time dictionary, add it to the date mentioned
			#If not, create a new entry
			if dateobject in timedict:
				oldtime = timedict[dateobject]
				newtime = int(timediff) + int(oldtime)
				print("Adding" + str(timediff) + " to " + str(oldtime))
				timedict[dateobject] = newtime
			else:
				timedict[dateobject] = int(timediff)
				print("new value" + str(timediff))	
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

		#Turns date into format similar to "Dec 30 23:38:51 2017"
		startdate_str = str((' '.join(split[4:8])))
		enddate_str = str((' '.join(split[10:14])))
		#Convert both of those dates to time objects
		startdate_obj = time.strptime(startdate_str, '%b %d %H:%M:%S %Y')
		enddate_obj = time.strptime(enddate_str, '%b %d %H:%M:%S %Y')

		#generate a month object that we will check against later
		dictmonth = {"Jan":"1", "Feb":"2","Mar":"3","Apr":"4","May":"5","Jun":"6","Jul":"7","Aug":"8","Sep":"9","Oct":"10","Nov":"11","Dec":"12"}

		#Test to see if starttime and endtime is in the same month
		#If it is, we simply add the two
		#If it is not, we add times respective to the enddate of the next month
		if startdate_str[0:3] != enddate_str[0:3]:
			modday = enddate_str[0:6] + " " + enddate_str[16::]
			nextday = time.strptime(modmonth, '%b %d %Y')

			#Previous Month (12:00 - XX:XX) time difference
			prvmonth_timediff = (time.mktime(nextday) - time.mktime(startdate_obj))
			prvmonth_timediff = str(round(prvday_timediff))

			#In this case, the dateobject will be the beginning section of our string
			month = str(split[4])
			month = dictmonth.get(month)

			dateobject = str(split[7]) + " " + month

			#Now, attempt to add it to our time dictionary
			if dateobject in timedict:
				oldtime = timedict[dateobject]
				newtime = int(prvday_timediff) + int(oldtime - 2)
				timedict[dateobject] = newtime
			else:
				timedict[dateobject] = str(prvday_timediff)

			#In this case, dateobject will be the end section of our string
			month = str(split[10])
			month = dictmonth.get(month)
			dateobject = str(split[13])	+ " " + month

			#Next Day (XX:XX - 12:00) Time Difference
			nxtday_timediff = (time.mktime(enddate_obj) - (time.mktime(nextday)))
			nxtday_timediff = str(round(nxtday_timediff))

			#Now, attempt to add it to our time dictionary
			if dateobject in timedict:
				oldtime = timedict[dateobject]
				newtime = int(prvday_timediff) + int(oldtime - 2)
				timedict[dateobject] = newtime
			else:
				timedict[dateobject] = str(prvday_timediff)

		else:
			month = str(split[4])
			month = dictmonth.get(month)
			dateobject = str(split[13])	+ " " + month
			dateobject = str(dateobject)

			#Get the time diffference between thsoe two dates, store it to timediff and round it
			#Get the difference between those dates, and store it to timediff
			timediff = (time.mktime(enddate_obj) - time.mktime(startdate_obj))
			print(time.mktime(enddate_obj))
			print(time.mktime(startdate_obj))
			timediff = round(timediff)
			timediff = str(timediff)
			#If entry is in our time dictionary, add it to the date mentioned
			#If not, create a new entry
			if dateobject in timedict:
				oldtime = timedict[dateobject]
				newtime = int(timediff) + int(oldtime)
				print(newtime)
				timedict[dateobject] = newtime
				print(timedict)
			else:
				timedict[dateobject] = str(timediff)
				print(timedict)
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
		total = total + value
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
		#If running with -l (E.g. ./ur.py -l user/host test.txt)
		if args.list is not None:
			#Since we are running with -l, the file that we are using is specified in the fourth argument
			subject = str(sys.argv[2])
			args.file = [str(sys.argv[3])]
			login_rec = read_login_rec(args.file,args)
			userhost_rec = get_login_rec(login_rec,args)
			
			line = str(args.list[0]) + " List for " + str(args.list[1]) #str(args.file).capitalize() + 
			eq = len(line)

			print(line)
			print("=" * eq)

			#Now that we are done, print the user or host involved by passing through each host/user in the list
			for user_or_host in userhost_rec:
				print(user_or_host)
		
		#If running with -r (E.g. ./ur.py -r 10.0.0.1 test.txt)
		if args.rhost or args.user is not None:
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