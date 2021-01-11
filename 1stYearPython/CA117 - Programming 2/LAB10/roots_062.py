#!/usr/bin/env python

import sys
import math

def roots(a, b, c):
	r1 = (-b + math.sqrt(b**2-(4*a*c))) /(2*a)
	r2 = (-b - math.sqrt(b**2-(4*a*c))) /(2*a)
	return r1, r2

def main():
	for line in sys.stdin:
		a, b, c = line.strip().split()
		try:
			(x, y) = roots(int(a), int(b), int(c))
			print('r1 = {}, r2 = {}'.format(x, y))
		except ValueError:
			print('None')

if __name__ == '__main__':
	main()