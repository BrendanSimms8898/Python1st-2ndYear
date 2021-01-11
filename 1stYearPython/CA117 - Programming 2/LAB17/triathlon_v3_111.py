#!/usr/bin/env python

class Triathlete(object):

	def __init__(self, name, tid):
		self.name, self.tid, self.times = name, tid, {}

	def add_time(self, sport, time):
		self.times[sport] = time

	def get_time(self, triathlete):
		return self.times[triathlete]

	def total_time(self):
		return sum(self.times.values())

	def __eq__(self, other):
		return (self.total_time() == other.total_time())

	def __gt__(self, other):
		return (self.total_time() > other.total_time())

	def __lt__(self, other):
		return (self.total_time() < other.total_time())

	def __str__(self):
		l = []
		l.append('Name: {}'.format(self.name))
		l.append('ID: {}'.format(self.tid))
		l.append('Race time: {}'.format(self.total_time()))
		return'\n'.join(l)

class Triathlon(object):

	def __init__(self):
		self.d = {}

	def add(self, Triathlete):
		self.d[Triathlete.tid] = Triathlete
		return self

	def remove(self, tid):
		del self.d[tid]
		return self

	def lookup(self, tid):
		if tid in self.d:
			return self.d[tid]
		return None

	def best(self):
		return min(self.d.values())

	def worst(self):
		return max(self.d.values())

	def sort_on_name(s):
		return s.name

	def __str__(self):
		l = []
		for x in sorted(self.d.values(), key=Triathlon.sort_on_name):
			l.append(str(x))
		return '\n'.join(l)

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    t2.add_time('swim', 300)
    t2.add_time('cycle', 100)
    t2.add_time('run', 200)

    t3.add_time('swim', 50)
    t3.add_time('cycle', 20)
    t3.add_time('run', 10)
    
    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn.best())
    print(tn.worst())

if __name__ == '__main__':
    main()
