#!/usr/bin/env python 

import sys

def camel_case(line):
	line = line.rstrip().split()
	i = 0
	while i < len(line):
		line[i] = line[i][0:-1] + line[i][-1].capitalize()
		i += 1
	print(" ".join(line))


def main():
	for line in sys.stdin:
		camel_case(line)


if __name__ == '__main__':
	main()