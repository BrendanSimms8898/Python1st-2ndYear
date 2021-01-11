#!/usr/bin/env python 

import sys

def mult3(n):
	return[c for c in n if not c % 3]

def mult3sqr(n):
	return[c ** 2 for c in n if not c % 3]

def mult4dbl(n):
	return[c * 2 for c in n if not c % 4]

def mult4ormult3(n):
	return[c for c in n if not c % 3 or not c % 4]

def mult4andmult3(n):
	return[c for c in n if not c % 3 and not c % 4]

def mult3replaced(n):
	b = n[:]
	for i in range(0, len(b)):
		if not b[i] % 3:
			b[i] = "X"
	return b

def isprime(n):
	for i in range(2,int(n**0.5)+1):
		if n % i == 0:
			return False
	return True

def prime(n):
	return[x for x in n if isprime(x)]

def main():
	n = [x for x in range(1, int(sys.argv[1]) + 1)]
	print('Multiples of 3: {}'.format(mult3(n)))
	print('Multiples of 3 squared: {}'.format(mult3sqr(n)))
	print('Multiples of 4 doubled: {}'.format(mult4dbl(n)))
	print('Multiples of 3 or 4: {}'.format(mult4ormult3(n)))
	print('Multiples of 3 and 4: {}'.format(mult4andmult3(n)))
	print('Multiples of 3 replaced: {}'.format(mult3replaced(n)))
	print('Primes: {}'.format(prime(n[1:])))


if __name__ == '__main__':
	main()