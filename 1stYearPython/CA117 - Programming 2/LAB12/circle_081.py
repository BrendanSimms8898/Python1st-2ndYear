#!/usr/bin/env python

class Point(object):

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def midpoint(self, other):
		mid_x = (self.x + other.x) / 2
		mid_y = (self.y + other.y) / 2
		mid_point = Point(mid_x, mid_y)
		return mid_point

class Circle(object):

	def __init__(self, centre=Point(0,0), radius=0):
		self.centre = centre
		self.radius = radius

	def __str__(self):
		return 'Centre: ({}, {})\nRadius: {}'.format(self.centre.x, self.centre.y, self.radius)

	def __add__(self, other):
		x = self.centre.midpoint(other.centre)
		y = self.radius + other.radius
		return Circle(x, y)


def main():
    p1 = Point()
    p2 = Point(4,6)
    c1 = Circle(p1, 10)
    c2 = Circle(p2, 5)
    c3 = c1 + c2
    print(c3)

    p3 = Point(10,10)
    c4 = Circle(p3,15)
    c5 = c2 + c4
    print(c5)
    
if __name__ == '__main__':
    main()



 