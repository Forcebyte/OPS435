#!/usr/bin/env python3

def join_lists(l1, l2):
	#join_sets will return a set that contains every value from both s1 and s2
	return(list(set(l1).union(set(l2))))

def match_lists(l1, l2):
	#match_sets will return a set that contains all values found in both s1 and s2
	return(list(set(l1).intersection(set(l2))))

def diff_lists(l1, l2):
	#diff_sets will return a set that contains all different values which are not shared between the sets
	set1 = set(l1)
	set2 = set(l2)
	
	runner = set1.symmetric_difference(set2)
	runner = list(runner)
	return(runner)
if __name__ == '__main__':
	list1 = list(range(1,10))
	list2 = list(range(5,15))
	print('list1: ', list1)
	print('list2: ', list2)
	print('join: ', join_lists(list1, list2))
	print('match: ', match_lists(list1, list2))
	print('diff: ', diff_lists(list1, list2))
