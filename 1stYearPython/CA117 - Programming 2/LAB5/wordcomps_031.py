#!/usr/bin/env python 

import sys 

def seventeen(words):
	return[c for c in words if len(c) == 17]

def seventeen_plus(words):
	return[c for c in words if len(c) >= 18]

def shortest_vowel(words):
	b = [x for x in words if 'a' in x and 'e' in x and 'i' in x and 'o' in x and 'u' in x]
	return min(b, key = len)

def four_a(words):
	return[c for c in words if c.lower().count('a') == 4]

def queues(words):
	return[c for c in words if c.count('q') >= 2 or c.count('Q') >= 2]

def cie(words):
	return[c for c in words if "cie" in c]

def anagram_of_angle(words):
	return[c for c in words if 'a' in c.lower() and 'n' in c.lower() and 'g' in c.lower() and 'l' in c.lower() and 'e' in c.lower() and len(c.lower()) == 5 and c.lower() != "angle"]

def end_iary(words):
	return len([c for c in words if c[-4:] == "iary"])

def q_without_u(words):	
	return[c for c in words if "q" in c.lower() and "qu" not in c.lower()]

def most_e(words):
	total = 0
	for line in words:
		f = line.count('e')
		if f > total:
			total = int(f)
	return[c for c in words if c.count('e') == int(total)]

def main():
	words = []
	for n in sys.stdin:
		n = n.strip()
		words.append(n)

	print('Words containing 17 letters: {}'.format(seventeen(words)))
	print('Words containing 18+ letters: {}'.format(seventeen_plus(words)))
	print('Shortest word containing all vowels: {}'.format(shortest_vowel(words)))
	print("Words with 4 a's: {}".format(four_a(words)))
	print("Words with 2+ q's: {}".format(queues(words)))
	print('Words containing cie: {}'.format(cie(words)))
	print('Anagrams of angle: {}'.format(anagram_of_angle(words)))
	print('Words ending in iary: {}'.format(end_iary(words)))
	print('Words with q but no u: {}'.format(q_without_u(words)))
	print("Words with most e's: {}".format(most_e(words)))


if __name__ == '__main__':
	main()