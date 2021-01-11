#!/usr/bin/env python 

import sys
import string 

def main():
	for line in sys.stdin:
		line = line.strip().casefold()
		print(palindrome(line))

def palindrome(x):
	 k = ''.join([i for i in x if i.isalnum()])

	 i = 0
	 while i < len(k): 
	 	if k[i] == k[len(k) - i - 1]:
	 		i = i + 1
	 	else: 
	 		return False

	 if i == len(k):
	 	return True
	 else: 
	 	return False

if __name__ == '__main__':
	main()