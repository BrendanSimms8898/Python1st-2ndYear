#!/usr/bin/env python 

import sys

def order(l):
	return l[1]

def main():
	skipped = []
	d = {}
	for line in sys.stdin:
		line = line.strip().split(':')
		name = line[0]
		rslt = line[1].split(',')
		total = 0
		try:
			for num in rslt:
				total = total + int(num)
			d[name] = total
		except ValueError:
			skipped.append(name)

	for (k, v) in sorted(d.items(), key = order, reverse = True):
		print('{} : {}'.format(k, v))
		
	print('Skipped:')
	for i in range(len(skipped)):
		print(skipped[i])
		
if __name__ == '__main__':
	main()