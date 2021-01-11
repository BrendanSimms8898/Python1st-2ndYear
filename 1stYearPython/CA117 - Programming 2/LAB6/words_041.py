#!/usr/bin/env python

import sys
import string

a = sys.stdin.read().lower().strip().split()
d = {}
for word in a:
	for ch in string.punctuation:
		ch = ch.strip(ch).strip('.')

	if word not in d:
		d[word] = 1
	else:
		d[word] += 1

a = sorted(d)
for i in range(0,len(a)):
	print('{} : {}'.format(a[i], d[a[i]]))