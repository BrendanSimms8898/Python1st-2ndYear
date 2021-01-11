#!/usr/bin/env python

import sys

def main():
	for line in sys.stdin:
		a = ''
		b = ''
		for word in line:
			if word.isupper():
				a = a + word
		if len(a):
			print(a)

if __name__ == '__main__':
		main()	