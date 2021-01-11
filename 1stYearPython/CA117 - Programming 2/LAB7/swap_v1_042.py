#!/usr/bin/env python

def swap_keys_values(d):
	new_dict = {}
	for key in d:
		new_dict[d[key]] = key

	return new_dict