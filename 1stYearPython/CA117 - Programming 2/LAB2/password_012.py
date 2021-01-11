#!/usr/bin/env python 

import sys 
import string

def main():
	for line in sys.stdin:
		line = line.strip()
		
		uppertotal = 0
		lowertotal = 0
		digittotal = 0
		symbltotal = 0

		for char in line:
			if char.isdigit() and digittotal == 0:
				digittotal = digittotal + 1
			elif char.isupper() and uppertotal == 0:
				uppertotal = uppertotal + 1
			elif char.islower() and lowertotal == 0:
				lowertotal = lowertotal + 1
			elif symbltotal == 0 and char in string.punctuation:
					symbltotal = symbltotal + 1
			

		print(uppertotal + lowertotal + digittotal + symbltotal)


if __name__ == '__main__':
	main()