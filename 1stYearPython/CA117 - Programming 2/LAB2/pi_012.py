#!/usr/bin/env python 

import sys
from math import pi

def main():
	x = sys.argv[1]
	print('{:.{}f}'.format(pi, x))


if __name__ == '__main__':
	main()