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

		#Generate a date object to use in the dictionary we will check against and later add to
		dictmonth = {"Jan":"1", "Feb":"2","Mar":"3","Apr":"4","May":"5","Jun":"6","Jul":"7","Aug":"8","Sep":"9","Oct":"10","Nov":"11","Dec":"12"}


		#If the entry is not on the same day, we take the median date between the two
		#After taking the median day, startdate usage is equal to the median day minus the startdate
		#Likewise, the ending day is just equal to the ending time...
		if startdate_str[4:6] != enddate_str[4:6]:
			modday = enddate_str[0:6] + " " + enddate_str[16::]
			nextday = time.strptime(modday, '%b %d %Y')

			#Previous day (12:00 - XX:XX) Time Difference
			prvday_timediff = (time.mktime(nextday) - time.mktime(startdate_obj))
			prvday_timediff = str(round(prvday_timediff))

			#In this case, dateobject will be the beginning section of our string
			month = str(split[4])
			month = dictmonth.get(month)
			dateobject = str(split[7]) + " " + month + " " + str(split[5])			
			#If entry is in our time dictionary, add it to the date mentioned
			#If not, create a new entry
			if dateobject in timedict:
				oldtime = timedict[dateobject]
				newtime = int(prvday_timediff) + int(oldtime) - 2
				print(newtime)
				timedict[dateobject] = newtime
				print(timedict)
			else:
				timedict[dateobject] = str(prvday_timediff)
				print(timedict)

			#In this case, dateobject will be the beginning section of our string
			month = str(split[10])
			month = dictmonth.get(month)
			dateobject = str(split[13]) + " " + month + " " + str(split[11])	

			#Next Day (XX:XX - 12:00) Time Difference
			nxtday_timediff = (time.mktime(enddate_obj) - (time.mktime(nextday)))
			nxtday_timediff = str(round(nxtday_timediff))

			if dateobject in timedict:
				oldtime = timedict[dateobject]
				newtime = int(nxtday_timediff) + int(oldtime)
				print(newtime)
				timedict[dateobject] = newtime
				print(timedict)
			else:
				timedict[dateobject] = str(nxtday_timediff)
				print(timedict)


		else:

			month = str(split[4])
			month = dictmonth.get(month)
			dateobject = str(split[7]) + " " + month + " " + str(split[5])
			dateobject = str(dateobject)

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
