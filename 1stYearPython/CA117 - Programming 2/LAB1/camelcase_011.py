#!/usr/bin/env python 

import sys

def camel_case(line):
	line = line.rstrip().split()
	i = 0
	while i < len(line):
		line[i] = line[i].capitalize()
		i += 1
	print(" ".join(line))


def main():
	for line in sys.stdin:
		camel_case(line)


if __name__ == '__main__':
	main()