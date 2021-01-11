#!/usr/bin/env python 

import sys

def main():
	names = []
	par = []
	hcap = []
	final = []

	x = [l.strip().split() for l in sys.stdin]

	par = x[0]
	idx = x[1]

	for line in x[2:]:
		n = " ".join(line[:-19])
		names.append(n)

		hcap = line[-18]
		shot = line[-18:]

		print(n)

if __name__ == '__main__':
	main()