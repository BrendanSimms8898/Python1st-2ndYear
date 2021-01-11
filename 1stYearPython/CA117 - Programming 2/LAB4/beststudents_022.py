#!/usr/bin/env python 

import sys

def main():
	a = []
	b = []
	try:
		with open(sys.argv[1], 'r' ) as f:
			for line in f:
				try:
					line = line.strip().split()
					mark = int(line[0])
					name = " ".join(line[1:])
					a.append(mark)
					b.append(name)

				except ValueError:
					print('Invalid mark {} encountered. Skipping.'.format(line[0]))					
			
			highest = 0
			i = 0
			while i < len(a):
				if int(a[i]) > highest:
					highest = int(a[i])
				i = i + 1

			c = []
				
			i = 0
			while i < len(a):
				if a[i] == highest:
					c.append(b[i])
				i = i + 1

			names = ", ".join(c)	

			print('Best student(s): {}'.format(names))
			print('Best mark:', highest)

	except FileNotFoundError:
		print('The file {} does not exist'.format(sys.argv[1]))

if __name__ == '__main__':
	main()	