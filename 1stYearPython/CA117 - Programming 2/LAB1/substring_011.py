#!/usr/bin/env python 

import sys

def main():
	for line in sys.stdin:
		line = line.strip().upper()
		token = line.split()
		if token[0] in token[1]:
			print("True")
		else:
			print("False")


if __name__ == '__main__':
	main()