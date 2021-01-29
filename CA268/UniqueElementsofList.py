def unique_list(a):
    return " ".join(set(a)).split()

#Test code provided by lecturer:
import sys
from sets import unique_list

def main():
    # Read in a list of strings
    lst = sys.stdin.readline().strip().split()

    # call the student's function ...
    answer = unique_list(lst)
    print(type(answer)) # should be a list
    answer.sort()
    print(answer)

if __name__ == "__main__":
    main()
    
#unique_list function returns a new list containing only the unique elements of the passed list
