#!/usr/bin/env python

import sys

def main():
		line = list(sys.argv[1])
		i = 0
		j = 1
		while j < len(line):
			line[i], line[j] = line[j], line[i]
			j += 2
			i = j - 1

		print("".join(line))

if __name__ == '__main__':
	main()