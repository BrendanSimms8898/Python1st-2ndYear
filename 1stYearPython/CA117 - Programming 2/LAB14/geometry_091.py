#!/usr/bin/env python

import math

class Point(object):

	def __init__(self, x=0, y=0):
		self.x, self.y = x, y

	def distance(self, other):
		return ((other.x - self.x)**2 + (other.y - self.y)**2)**0.5

class Shape(object):

	def __init__(self, points=[]):
		self.points = points

	def sides(self):
		lengths = []
		for i in range(1, len(self.points)):
			lengths.append(self.points[i-1].distance(self.points[i]))
		lengths.append(self.points[-1].distance(self.points[0]))
		return lengths

	def perimeter(self):
		l = self.sides()
		return sum(l)

class Triangle(Shape):

	def area(self):
		l = self.sides()
		a, b, c = l[0], l[1], l[2]

		s = (a + b + c) / 2

		return math.sqrt((s * ((s -a)*(s-b)*(s-c))))


class Square(Shape):

	def area(self):
		l = self.sides()
		return (l[0] ** 2)

def main():

    t1 = Triangle([Point(0,0), Point(3,4), Point(6, 0)])
    print(t1.sides())
    print(t1.perimeter())
    print(t1.area())

    t2 = Triangle([Point(0,0), Point(4,0), Point(4, 3)])
    print(t2.sides())
    print(t2.perimeter())
    print(t2.area())

    s1 = Square([Point(0,0), Point(5,0), Point(5,5), Point(0,5)])
    print(s1.sides())
    print(s1.perimeter())
    print(s1.area())

if __name__ == '__main__':
    main()
