#!/usr/bin/env python

class Score(object):

	def __init__(self, goals=0, points=0):
		self.goals = goals
		self.points = points

   def goals_to_points(self):
      return self.goals * 3 + self.point

   def __str__(self):
      return '{} goal(s) and {} point(s)'.format(self.goals, self.points)

   def __eq__(self, other):
      return self.goals_to_points() == other.goals_to_points()

   def __gt__(self, other):
      return self.goals_to_points() > other.goals_to_points()

   def __lt__(self, other):
      return self.goals_to_points() < other.goals_to_points()

   def __ge__(self,other):
      return (self.goals_to_points() <= other.goals_to_points())

   def __le__(self,other):
      return (self.goals_to_points() >= other.goals_to_points())

   def __add__(self,other):
      x = self.goals + other.goals
      y = self.points + other.points 
      return Score(x, y)

   def __sub__(self, other):
      x = self.goals - other.goals
      y = self.points - other.points
      return Score(x, y)

   def __iadd__(self, other):
      x = self + other
      self.goals, self.points = x.goals, x.points
      return self

   def __isub__(self, other):
      x = self - other
      self.goals, self.points = x.goals, x.points
      return self

   def __mul__(self, other):
      x = self.goals * other
      y = self.points * other
      return Score(x, y)

   def __imul__(self, other):
      x = self * other
      self.goals, self.points = x.goals, x.points
      return self
