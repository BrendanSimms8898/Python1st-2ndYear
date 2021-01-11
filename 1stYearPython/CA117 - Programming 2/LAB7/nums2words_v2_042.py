#!/usr/bin/env python

import sys 

def n(x):
	d = {
		"0" : "zero",
		"1" : "one",
		"2" : "two",
		"3" : "three",
		"4" : "four",
		"5" : "five",
		"6" : "six",
		"7" : "seven",
		"8" : "eight",
		"9" : "nine",
		"10": "ten",
	} 
	if x not in d:
		return "unknown"
	else:
		return d[x]

def main():
	s = ""
	for line in sys.stdin:
		line = line.strip().split()
		for x in line:
			s += "{} ".format(n((x)))
		print(s.strip())
		s = ""



if __name__ == '__main__':
	main()