#!/usr/bin/env python

class Triathlete(object):

	def __init__(self, name, tid):
		self.name, self.tid = name, tid
		self.times = {}

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