#!/usr/bin/env python 

import sys

def consonant(line):
	vowel = ["a","e","i","o","u"]
	if line[-2] not in vowel:
		return True

def plural(line):

	ess = ["x","s","z"]
	es = ["ch", "sh"]

	for char in line:

		if consonant(line) and line[-1] == "y":
			line = line[:-1] + "ies"
			return line
		elif line[-1] == "f":
			line = line[:-1] + "ves"
			return line
		elif line[-2:] == "fe":
			line = line[:-2] + "ves"
			return line
		elif line[-1] == "o":
			line = line + "es"
			return line
		elif line[-2:] in es:
			line = line + "es"
			return line
		elif line[-1] in ess:
			line = line + "es"
			return line
		else:
			line = line + "s"
			return line


 

def main():
	for line in sys.stdin:
		print(plural(line.strip()))

if __name__ == '__main__':
	main()