#!/usr/bin/env python

import sys 
import string

def main():
	words = []

	for line in sys.stdin:
		for word in line.lower().strip().split():
			for ch in word.strip():
				if ch in string.punctuation:
					word = word.replace(ch, "")
				if word not in words and word.isalnum():
					words.append(word)

	print(len(words))


if __name__ == '__main__':
	main()