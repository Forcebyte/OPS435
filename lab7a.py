#!/usr/bin/env python3

# Store one IPv4 address
class IPAddress:
    # You probably want to construct it as a string, but you may want to store it as the four octets separately:
	def __init__(self, address):
		x = address.index('.')
		self.octet1 = address[:x]
		a2 = address[x+1:]
		x2 = address.index('.')
		self.octet2 = a2[:x2]
		a3 = address[x+x2+1:]
		x3 = address.index('.')
		self.octet3 = a3[:x3]
		
    # Is this address from a private subnet? e.g. starting with 192.168. or 10.
	def isPrivate(self):
		if self.octet1 == '192' and self.octet2 == '168':
			return 'True'
		elif self.octet1 == '10':
			return 'True'
		else:
			return 'False'

class Person:
	def __init__(self, name):
		x = name.split(' ')
		self.firstname = x[0]
		self.lastname = x[1]

class BMWModel:
	def __init__(self, car):
		CarMake = self.car.split[0:3]
		CarSeries = self.car.split[3:8]

class Car:
	def __init__(self, specs):
		CarOwn = self.specs.split[0:7]
		CarType = self.specs.split[7:11]
		CarVIN = self.specs.split[11:20]

if __name__ == '__main__':
	ip1 = IPAddress('192.168.70.1')
	ip1.isPrivate()
	ip2 = IPAddress('192.168.1.10')
	ip2.isPrivate()
	ip3 = IPAddress('10.0.0.50')
	ip3.isPrivate()
	ip4 = IPAddress('142.203.1.2')
	ip4.isPrivate()
	Person = Person('Andrew Oatley-Willis')
	Person2 = Person('Murray Saul')
	Person3 = Person('Andrew Smith')
	# BMWModel = car('BMW2Series')
	# BMWModel2 = car('BMW3Series')
	# BMWModel3 = car('BMW4Series')
	# BMWModel4 = car('BMWXSeries')
	# BMWModel5 = car('BMWMSeries')
	# BMWModel6 = car('BMWiSeries')
	# Car = specs("Andrew's silver Civic with VIN 1234567890")
	# Car2 = specs("John's blue Subaru with VIN 0987654321")
	# Car3 = specs("Evan's BWMMSeries with VIN 4567981230")