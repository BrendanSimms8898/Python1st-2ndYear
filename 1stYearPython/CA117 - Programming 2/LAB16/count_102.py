#!/usr/bin/env python

def count_letters(s):
	total = 0
	if s == '':
		return 0
	else:
		return 1 + count_letters(s[1:])