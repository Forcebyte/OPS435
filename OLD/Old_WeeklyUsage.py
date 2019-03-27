def cal_monthly_usage(login_recs, args):
	'''
	cal_monthly_usage(login_recs) -> timedict
		takes the login record lines generated in read_login_rec, and calculates the monthly usage of each user or host mentioned
		finally, it returns a dictionary with each month, and the total time for that month
		Note that this function depends on parse_time, as it calculates time's down to the second for outputting

		e.g. cal_monthly_usage(login_recs) -> Dictionary of time totals
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

		timestart = split[6]
		timeend = split[12]

		#Parse time gets the number of seconds in a date statement
		timestartsec = parse_time(str(timestart))
		timeendsec = parse_time(str(timeend))

		timedelta = timeendsec - timestartsec

		#String is as follows...
		#SPLIT[7] = Year YYYY
		#SPLIT[4] = Month (Apr)
		#SPLIT[5] = Day DD

		#Since we can't use datetime, convert the month spelling to a number
		dictmonth = {"Jan":"1", "Feb":"2","Mar":"3","Apr":"4","May":"5","Jun":"6","Jul":"7","Aug":"8","Sep":"9","Oct":"10","Nov":"11","Dec":"12"}
		month = str(split[4])
		month = dictmonth.get(month)

		#Parse the date object
		dateobject = str(split[7]) + " " + str(split[4]) + " " + str(split[5])
		dateobjectstring = split[7] + " " + month
		
		#If the date exists, add the number of seconds along with the old time
		#If it doesn't add a new entry to timedict
		if dateobjectstring in timedict:
			oldtime = timedict[dateobjectstring]
			newtime = timedelta + int(oldtime)
			timedict[dateobjectstring] = newtime
			#timedict[str(dateobject)] = [timedict[str(dateobject)], str((timedelta + int(timedict.get(str(dateobject)))))]
		else:
			#minhour = str(split[-1])
			timedict[dateobjectstring] = str(timedelta)
	return(timedict)