#!/usr/bin/env python

def maximum(l = []):
	if len(l) == 1:
		return l[0]
	else:
		if l[0] > maximum(l[1:]):
			return l[0]
		else:
			return maximum(l[1:])