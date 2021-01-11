#!/usr/bin/env python

import sys 

words = [line.strip() for line in sys.stdin]

def reverse(s, words):
	lo = 0
	hi = len(words) - 1
	while lo < hi:
		mid = (lo + hi) // 2
		if s[::-1].lower() > words[mid].lower():
			lo = mid + 1
		else:
			hi = mid
	return words[lo].lower() == s[::-1].lower() and len(s) > 4

print([word for word in words if reverse(word,words)])
