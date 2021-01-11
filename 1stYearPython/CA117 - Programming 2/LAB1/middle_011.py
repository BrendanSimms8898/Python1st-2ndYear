#!/usr/bin/env python 

import sys 

def main():
	for line in sys.stdin:
		line = line.strip()
		if len(line) % 2 == 0: 
			print("No middle character!")
		elif len(line) % 2 == 1:
			print(line[len(line) // 2])


if __name__ == '__main__':
	main()