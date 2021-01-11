#!/usr/bin/env python 

import sys

def longest_line(a):
    len1 = 0
    for line in a:
        if len(line) > len1:
            len1 = len(line.strip())
    return len1

def main():
    #x = longest_line(a)
    #a = sys.stdin.readlines()
    for line in sys.stdin:
        line = line.strip().split()
        posclub = line[0]
        scores = line[-7:]
        club = line[1:-8]
        club = " ".join(club)
        print(scores)
        



if __name__ == '__main__':
	main()