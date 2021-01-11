#!/usr/bin/env python 

import sys 

def main():
	for line in sys.stdin:
		line = line.strip().split()

		word1 = line[0]
		word2 = line[1]

		if len(word1) == len(word2):
			print(True)
		else:
			print(False)

if __name__ == '__main__':
	main()