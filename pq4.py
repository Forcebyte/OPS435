#!/usr/bin/env python3
import sys
filename = sys.argv[1]

try:
	file = open(filename,'r')
	linelist = file.read().splitlines()
	file.close()
	lee = []
	for item in linelist:
		if item:
			print(item)
			lee.append(item)
	print("Total number of non-blank lines in file: " + str(len(lee)))
except FileNotFoundError:
	print("File Error: File " + str(filename) + " does not exist")
except PermissionError:
	print("File Error: Do not have permission to read " + str(filename))
