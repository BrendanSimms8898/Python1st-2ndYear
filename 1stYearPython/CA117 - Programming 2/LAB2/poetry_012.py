#!/usr/bin/env python 

import sys 

def longest_line(a):
	len1 = 0
	for line in a:
		if len(line) > len1:
			len1 = len(line.strip())
	return len1

def main():
	a = sys.stdin.readlines()
	x = longest_line(a)
	for line in a:
		print('{:^{}s}'.format(line.strip(), x))

if __name__ == '__main__':
	main()












