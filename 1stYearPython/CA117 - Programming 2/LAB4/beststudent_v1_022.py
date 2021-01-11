#!/usr/bin/env python 

import sys

def main():
	a = []
	b = []
	try:
		with open(sys.argv[1], 'r' ) as f:
			for line in f:
				line = line.strip().split()
				mark = line[0]
				name = " ".join(line[1:])
				a.append(mark)
				b.append(name)

			highest = 0
			i = 0
			j = 0
			while i < len(a):
				if int(a[i]) > highest:
					highest = int(a[i])
					j = i
				i = i + 1

		print('Best student:', b[j])
		print('Best mark:', highest)

	except FileNotFoundError:
		print('The file {} does not exist'.format(sys.argv[1]))

if __name__ == '__main__':
	main()	