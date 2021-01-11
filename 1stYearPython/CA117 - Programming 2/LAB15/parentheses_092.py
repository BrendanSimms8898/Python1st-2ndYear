#!/usr/bin/env python

import sys
from stack_092 import Stack

def main():

    for line in sys.stdin:
        print(matcher(line.strip()))


def matcher(x):
	if x.count('(') == x.count(')'):
		if x.count('{') == x.count('}'):
			if x.count('[') == x.count(']'):
				return True	
	
	return False

if __name__ == '__main__':
    main()

