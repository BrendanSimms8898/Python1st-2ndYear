#!/usr/bin/env python

import sys

def build_dictionary(filename):
	d = {}
	with open(filename, 'r') as f:
		for x in f:
			[word, number] = x.strip().split()
			d[word] = number
	return d

def extract_range(d, n, x):
	nd = {}
	for (k, v) in sorted(d.items()):
		if int(v) >= n and int(v) <= x:
			nd[k] = int(v)
	return nd
