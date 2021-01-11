#!/usr/bin/env python 

import sys

def main():
	for line in sys.stdin:
		a = line.strip().split()[0]
		b = line.strip().split()[1]
		print (int(a, int(b)))



if __name__ == '__main__':
	main()