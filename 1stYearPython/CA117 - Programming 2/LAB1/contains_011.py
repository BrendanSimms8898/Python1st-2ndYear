#!/usr/bin/env python 

import sys

def main():
	for line in sys.stdin:
		line = line.strip().lower()
		a = line.split()[0]
		b = line.split()[1]
		check = True
		
		for ch in a:
			if ch in b:
				b = b.replace(ch, " ")
			else:
				check = False
		print(check)
	

if __name__ == '__main__':
	main()