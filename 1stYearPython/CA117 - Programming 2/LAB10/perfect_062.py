#!/usr/bin/env python

import sys

def sumFac(n):
    return sum({x for x in range(1, n // 2 + 1) if not n % x})

def isPerfect(n):   
    return sumFac(n) == n
    
def main():
    for line in sys.stdin: 
        line = line.strip()
        print(isPerfect(int(line)))


if __name__ == '__main__':
      main()  