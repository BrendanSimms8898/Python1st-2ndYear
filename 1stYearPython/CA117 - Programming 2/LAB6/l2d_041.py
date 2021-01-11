#!/usr/bin/env python

def l2d(x):
	d = {}
	lists = []
	for line in x:
		lists.append(line)
	word = lists[0].split()
	ints = lists[1].split()
	j = 0
	for i in range(len(word)):
		d[word[j]] = ints[j]
		j += 1
	return d
