#!/usr/bin/env python

import sys

def main():
	for line in sys.stdin:
		word = line.strip().lower()
		t = ""
		for x in word:
			if x == "e":
				t = t + "b"
			elif x == "v":
				t = t + "l"
			elif x == "i":
				t = t + "o"
			elif x == "l":
				t = t + "t"
		if t == "blot":
			print(line.strip())

if __name__ == '__main__':
	main()