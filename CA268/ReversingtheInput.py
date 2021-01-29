from Stack import Stack
import sys

def reverse_input(stack):
    for line in sys.stdin:
        stack.push(line.strip())
    while not stack.is_empty():
        print(stack.pop())

#Example stack class:
class Stack:
#
#  Stack ADT has three methods: is_empty, push and pop.
#
   def __init__(self):
      self.stack = []
      self.top = 0

   def is_empty(self):
      return self.top == 0

   def push(self, item):
      if self.top < len(self.stack):
         self.stack[self.top] = item
      else:
         self.stack.append(item)

      self.top += 1

   def pop(self):
      if self.is_empty():
         return None
      else:
         self.top -= 1
         return self.stack[self.top]
        
 #example code to test function
from Stack import Stack
from reverse_input import reverse_input

stack = Stack()
reverse_input(stack)
