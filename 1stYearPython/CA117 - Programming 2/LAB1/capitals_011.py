#!/usr/bin/env python 

import sys 

def main():
	for line in sys.stdin:
		line = line.strip()
		if len(line) > 1:
			print (line[0].capitalize() + line[1:-1] +line[-1].capitalize())

if __name__ == '__main__':
	main()
	
#Code to Capatilize the first letter in stdin and reprint with capitalization in effect
