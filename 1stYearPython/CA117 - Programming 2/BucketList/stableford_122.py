#!/usr/bin/env python 

import sys

def order(l):
	return l[1]

def main():
	final = {}
	discq = []
	names = []

	x = [l.strip().split() for l in sys.stdin]

	par = x[0]
	idx = x[1]

	h_order = [idx.index(str(i)) for i in range (1, 19)]

	for line in x[2:]:
		n = " ".join(line[:-19])
		names.append(n)

		hcap = int(line[-19])
		shot = line[-18:]
		
		for i in range(0, hcap):
			if shot[h_order[i%18]].isnumeric():
				shot[h_order[i%18]] = str(int(shot[h_order[i%18]]) - 1)

		score = 0
		for i in range(0, 18):
			if shot[i].isnumeric() and int(shot[i]) - int(par[i]) < 2:
				score += 2 - (int(shot[i]) - int(par[i]))
			elif not shot[i].isnumeric() and shot[i] != "X":
				discq.append(n)
				break
		if n not in discq:
			final[n] = score

	width = max([len(n) for n in names])		
				
	for (k,v) in sorted(final.items(), key = order, reverse = True):		
		print('{:>{}} : {:>2}'.format(k, width, v))

	for n in discq:
		print('{:>{}} : Disqualified'.format(n, width)) 	

if __name__ == '__main__':
	main()