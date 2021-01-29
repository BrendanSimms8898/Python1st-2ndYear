def set_stuff(seta, setb):
	return(seta | setb, seta & setb == seta, setb & seta == setb)

#Test code provided by lecturer:
import sys
from sets import set_stuff

# Function to make a set from a string of tokens
def make_set(line):
    line = line.strip()
    tokens = line.split()
    return set(tokens)

def make_sorted_list(s):
    lst = list(s)
    lst.sort()
    return lst

def main():
    # Read each set
    line1 = sys.stdin.readline()
    a = make_set(line1)

    line2 = sys.stdin.readline()
    b = make_set(line2)

    # call the student's function ...
    union, sub, super = set_stuff(a, b)

    # ... and print the result
    # First convert to a list and sort to be sure that the order will always be the same
    print(make_sorted_list(union))
    print(sub)
    print(super)

if __name__ == "__main__":
    main()

#Function set_stuff returns: 
#1. The union of the two sets a and b.
#2. A boolean value, True or False, depending on whether a is a subset of b.
#3. A boolean value, True or False, depending on whether a is a superset of b.