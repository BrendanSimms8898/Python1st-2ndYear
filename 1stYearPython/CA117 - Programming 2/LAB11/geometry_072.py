#!/usr/bin/env python

import math

class Point(object):

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def distance(self, other):
		return math.sqrt(((other.x - self.x)**2) + ((other.y - self.y)**2))

	def __str__(self):
		return "({:.1f}, {:.1f})".format(self.x, self.y)

class Segment(object):

	def __init__(self, p1, p2):
		self.p1 = p1 #(0,0)
		self.p2 = p2 #(5,5)

	def midpoint(self):
		mid_x = (self.p1.x + self.p2.x) / 2	#self.p1.x = x1 ---- self.p2.y = x2
		mid_y = (self.p1.y + self.p2.y) / 2 #self.p1.y = y1 ---- self.p2.y = y2
		mid_point = Point(mid_x, mid_y)
		return mid_point

	def length(self):
		return math.sqrt(((self.p2.x - self.p1.x) **2) + ((self.p2.y - self.p1.y) **2))
		 
class Circle(object):

	def __init__(self, centre, radius=0):
		self.centre = centre
		self.radius = radius
		
	def overlaps(self, other):
		return ((self.centre.x - other.centre.x) ** 2) + ((self.centre.y - other.centre.y) ** 2) < ((self.radius + other.radius) ** 2) 

def main():
    p1 = Point()
    p2 = Point(5, 5)
    s1 = Segment(p1, p2)
    s2 = Segment(p2, p1)
    c1 = Circle(p1, 5)
    c2 = Circle(p2, 2)
    c3 = Circle(p1, 2)

    print(p1)
    print(p2)
    print(s1.midpoint())
    print(s2.midpoint())
    print(c1.overlaps(c2))
    print(c2.overlaps(c1))
    print(c1.overlaps(c3))
    print(c3.overlaps(c2))

if __name__ == '__main__':
    main()
