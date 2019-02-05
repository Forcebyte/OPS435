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

def append_file_string(file_name, string_of_lines):
    # Takes a filename string, and appends string to end of the file
	file = open(file_name,'a')
	file.write(string_of_lines)
	file.close()
def write_file_list(file_name, list_of_lines):
    # Takes a filename strin and list of lines and overwrites all data found in list to file
	file = open(file_name,'w')
	for line in list_of_lines:
		file.write("%s\n" % line)
	file.close()

def copy_file_add_line_numbers(file_name_read,file_name_write):
    # Takes two strings, reads data from first file, writes data to a new file, adds line # to new file
	file = open(file_name_read,'r')
	alllines = file.read().splitlines()
	file.close()

	file = open(file_name_write,'w')
	counter = 1
	for line in alllines:
		file.write(str(counter) + ":" + str(line) + "\n")
		counter = counter + 1
	file.close()
	return 
if __name__ == '__main__':
	file1 = 'seneca1.txt'
	file2 = 'seneca2.txt'
	file3 = 'seneca3.txt'
	string1 = 'First Line\nSecond Line\nThird Line\n'
	list1 = ['Line 1', 'Line 2', 'Line 3']
	append_file_string(file1, string1)
	print(read_file_string(file1))
	write_file_list(file2, list1)
	print(read_file_string(file2))
	copy_file_add_line_numbers(file2, file3)
	print(read_file_string(file3))
