#!/usr/bin/env python3

def read_file_string(file_name):
    # Takes a filename string, returns a string of all lines in the file
	file = open(file_name,'r')
	alllines = file.read()
	file.close()
	return(alllines)
def read_file_list(file_name):
    # Takes a filename string, returns a list of lines without new-line characters
	file = open(file_name,'r')
	linelist = file.read().splitlines()
	file.close()
	return(linelist)
if __name__ == '__main__':
	file_name = 'data.txt'
	print(read_file_string(file_name))
	print(read_file_list(file_name))
