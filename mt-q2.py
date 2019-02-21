#!/usr/bin/env python3

import sys
list1 = []

for item in sys.argv[:0:-1]:
	list1.append(item)
	print(item)
print("LIst provided: " + str(list1))
