#!/usr/bin/env python

class Employee(object):

	def __init__(self, name, number=0):
		self.name, self.number = name, number

	def wages(self):
		return 0.0

	def __str__(self):
		l = []
		l.append('Name: {}'.format(self.name))
		l.append('Number: {}'.format(self.number))
		l.append('Wages: {:.2f}'.format(self.wages()))
		return '\n'.join(l)

class Manager(Employee):

	def __init__(self, name, number=0, salary=0):
		super().__init__(name, number)
		self.salary = salary

	def wages(self):
		super().wages()
		return self.salary / 52

class AssemblyWorker(Employee):

	def __init__(self, name, number=0, per_hour=0, hours=0):
		super().__init__(name, number)
		self.per_hour, self.hours = per_hour, hours

	def wages(self):
		super().wages()
		return self.per_hour * self.hours 

def main():

    e1 = Manager('Mary', 1, 50000)
    e2 = AssemblyWorker('Fred', 2, 15.50, 40)
    e3 = Employee('Sean', 3)

    print(e1)
    print(e2)
    print(e3)

if __name__ == '__main__':
    main()
