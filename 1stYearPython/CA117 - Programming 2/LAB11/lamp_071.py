#!/usr/bin/env python

class Lamp(object):

	def __init__(self, on=False):
		self.on = on

	def turn_on(self):
		return self.on == True



	def turn_off(self):
		return self.on == False

	def toggle(self):
		self.on = not self.on
		return not self