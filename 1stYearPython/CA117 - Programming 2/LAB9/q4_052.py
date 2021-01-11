#!/usr/bin/env python

import sys

def main():
	d = {}
	with open(sys.argv[1], 'r') as f:
		for line in f:
			line = line.strip().split()
			food = " ".join(line[:-1])
			cals = line[-1]
			d[food] = int(cals)

	nd = {}
	for x in sys.stdin:
		x = x.strip().split(',')
		name = " ".join(x[:1])
		meal = x[1:]
		nd[name] = 0
			
		for a in meal:
			if a in d:
				nd[name] += d[a]
			else:
				nd[name] += 1
	
	for (k, v) in sorted(nd.items()):
		l_name 



if __name__ == '__main__':
	main()

