#!/usr/bin/env python

import sys
import string

a = sys.stdin.read().lower().strip().split()
d = {}
nd = {}
for word in a:
	for ch in string.punctuation:
		word = word.strip(ch).strip(".")

	if word not in d and len(word) >= 3:
		d[word] = 0
	if word in d:
		d[word] += 1

	for (k,v) in sorted(d.items()):
		if v >= 3 and len(k) > 3:
			nd[k] = v

w_width = len(max(nd, key=len))

n_width = 0
for (k, v) in sorted(d.items()):
	if len(str(v)) > n_width:
		n_width = len(str(v))
	
for (x, y) in sorted(nd.items()):
	print('{:>{:d}s} : {:{:d}d}'.format(x, w_width, y, n_width))
