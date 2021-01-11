#!/usr/bin/env python

import sys

def translate(word):
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
		"10": "ten"
		}
	
	return d[word]

def main():
	t = {}
	with open(sys.argv[1], 'r') as f:
		for line in f:
			line = line.strip().split()
			t[line[0]] = line[1]
	s = ""
	for line in sys.stdin:
		line = line.strip().split()
		for x in line:
			s += "{} ".format(t[translate(x)])
		print(s.strip())
		s = ""

if __name__ == '__main__':
	main()