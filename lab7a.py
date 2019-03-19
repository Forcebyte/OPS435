#!/usr/bin/env python3

# Store one IPv4 address
class IPAddress:
	# You probably want to construct it as a string, but you may want to store it as the four octets separately:
	def __init__(self, address):
		splitter = address.split('.') 
		self.octet1 = splitter[0]
		self.octet2 = splitter[1]
		self.octet3 = splitter[2]
		self.octet4 = splitter[3]

	# Is this address from a private subnet? e.g. starting with 192.168. or 10.
	def isPrivate(self):
		if (str(self.octet1) == "192") and (str(self.octet2) == "168"):
			return True
		elif str(self.octet1) == "10":
			return True
		else:
			return False 

# Store information about a person, perhaps someone you'll be adding as a user to a system:
class Person:
	def __init__(self,name,idnum):
		namesplit = name.split(' ')
		self.firstname = namesplit[0]
		self.lastname = namesplit[1]

		self.idnum = idnum

	def displaystudent(self):
		print("Hi there " + str(self.firstname) + ", your student number is " + str(self.idnum))
# Store information about different models from a specific manufacturer. Perhaps how many seats they have and how much fuel they use and the price range:
# Doesn't have to be BMW, pick any car or bike manufacturer:
class BMWModel:
	def __init__(self,Model,seatcapacity):
		self.model = Model
		self.seatcapacity = seatcapacity

	def issixseater(self):
		if int(self.seatcapacity) == 6:
			print(str(self.model) + " is a Six Seater Car")
		else:
			print(str(self.model) + " is not a Six Seater Car")
# Store information about a specific car that someone owns.
# Spend some time thinking why this class is different than the one above, and whether it has to be different:
class Car:
	def __init__(self,Bulkinfo):
		splitter = Bulkinfo.split(' ')
		self.carowner = splitter[0]
		self.carmake = splitter[1:2]
		self.vin = splitter[-1]

if __name__ == '__main__':

	ip1 = IPAddress('192.168.70.1')
	if ip1.isPrivate():
		print("Is Private")
	else:
		print("Is not Private")
	
	ip2 = IPAddress('200.100.52.1')
	if ip2.isPrivate():
		print("Is Private")
	else:
		print("Is not Private")

	Person1 = Person("Patrick Turney","114850167")
	Person2 = Person("Andrew Willus","1111")
	Person1.displaystudent()
	Person2.displaystudent()

	car1 = BMWModel("Audi X8",6)
	car2 = BMWModel("Chevy Volt",4)

	car1.issixseater()
	car2.issixseater()

	car1details = Car("Evan's BWMMSeries with VIN 4567981230")
	car2details = Car("John's blue Subaru with VIN 0987654321")

	print("Car 2's VIN is " + str(car2details.vin))
