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

		#Turns date into format similar to "Dec 30 23:38:51 2017"
		startdate_str = str((' '.join(split[4:8])))
		enddate_str = str((' '.join(split[10:14])))
		#Convert both of those dates to time objects
		startdate_obj = time.strptime(startdate_str, '%b %d %H:%M:%S %Y')
		enddate_obj = time.strptime(enddate_str, '%b %d %H:%M:%S %Y')

		#Grab a week number from each entry to compare (%U is week number from 0-51)
		startdate_wk = str(strftime("%U", startdate_obj))
		enddate_wk = str(strftime("%U", enddate_obj))

		#Since week 1 is 0, we add 1 to the weeknumber to get our actual week
		startdate_wk =str(int(startdate_wk) + 1)
		enddate_wk = str(int(enddate_wk) + 1)

		#generates a date object to use in the dictionary we will comapre to
		#dictmonth = {"Jan":"1", "Feb":"2","Mar":"3","Apr":"4","May":"5","Jun":"6","Jul":"7","Aug":"8","Sep":"9","Oct":"10","Nov":"11","Dec":"12"}

		#If the entry is not on the same week, we take the median date between the two
		#After taking the median day, startdate usage is equal to the median day minus the startdate
		#Likewise, the ending day is just equal to the ending time...
		if startdate_wk != enddate_wk:
			modday = enddate_str[0:6] + " " + enddate_str[16::]
			print(modday)
			nextday = time.strptime(modday, '%b %d %Y')

			#Previous day (12:00 - XX:XX) time difference, take it and round it out
			prvday_timediff = (time.mktime(nextday) - time.mktime(startdate_obj))
			prvday_timediff = str(round(prvday_timediff))

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
			#Next Day (XX:XX - 12:00) Time Difference
			nxtday_timediff = (time.mktime(enddate_obj) - (time.mktime(nextday)))
			nxtday_timediff = str(round(nxtday_timediff))

			if dateobject in timedict:
				oldtime = timedict[dateobject]
				newtime = int(nxtday_timediff) + int(oldtime) - 2
				timedict[dateobject] = newtime
			else:
				timedict[dateobject] = str(nxtday_timediff)
		else:
			dateobject = str(split[13]) + " " + str(startdate_wk)
			dateobject = str(dateobject)

			#Get the difference between those dates, and store it to timediff
			timediff = (time.mktime(enddate_obj) - time.mktime(startdate_obj))
			timediff = round(timediff)
			timediff = str(timediff)
			#If entry is in our time dictionary, add it to the date mentioned
			#If not, create a new entry
			if dateobject in timedict:
				oldtime = timedict[dateobject]
				newtime = int(timediff) + int(oldtime)
				timedict[dateobject] = newtime
			else:
				timedict[dateobject] = str(timediff)
	return(timedict)