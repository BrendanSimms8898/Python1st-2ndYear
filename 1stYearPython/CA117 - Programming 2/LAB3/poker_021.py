#!/usr/bin/env python 

import sys

def main():
	t = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	hand = {
		0 : "nothing",
		1 : "one pair",
		2 : "two pairs",
		3 : "three of a kind",
		4 : "a straight",
		5 : "a flush",
		6 : "a full house",
		7 : "four of a kind",
		8 : "a straight flush",
		9 : "a royal flush",
	}

	for line in sys.stdin:
		t[int(line.strip()[-1])] += 1
		t[10] += 1

	i = 0
	while i < 10:
		print('The probability of {:s} is {:.4f}%'.format(hand[i], float(((t[i] / t[10])*100))))
		i += 1
		
if __name__ == '__main__':
	main()