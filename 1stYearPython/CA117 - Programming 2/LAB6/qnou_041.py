#!/usr/bin/env python 

import sys

def q_without_u(words):
	qs = "qu"
	for ch in words:
		if qs in ch:
			ch = ch.replace("", ch)
			if "q" in ch.lower():

				return list(words)

def main():
	words = []
	for n in sys.stdin:
		n = n.strip()
		words.append(n)
	
		print("Words with q but no u: {}".format(q_without_u(words)))

if __name__ == '__main__':
	main()