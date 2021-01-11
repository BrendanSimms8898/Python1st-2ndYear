#!/usr/bin/env python 

import sys 

def chop(s):
	return s[1:len(s)-1]

def main(): 
	for line in sys.stdin:
		cs = chop(line.strip())
		if len(cs) > 0:
			print(cs)

if __name__ == '__main__':
	main()