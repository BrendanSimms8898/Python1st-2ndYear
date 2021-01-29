import sys
def make_map():
	d = {}
	for line in sys.stdin.read().split("\n"):
		if len(line) > 0:
			line = line.strip().split()
			d[line[0]] = line[-1]
	return d

#A function called make_map() which reads data from the input and creates and returns a map. 
#The program should read student details from standard input, one line per student. Each line contains a student name followed by a mark.

#Example Program used to call method:
# import the student function
#from student_marks import make_map
#from sys import argv  # Even though we don't need argv in this exercise

#def main(argv):
    #student = make_map() # Call the student function
    #print(type(student)) # check the type ... should be a map (or in python, dict)
    #names = student.keys()   # get all names
    #for name in sorted(names): # sort the names
        #print(name + " has mark " + student[name]) # print the names and marks
    
#if __name__ == "__main__":
    #main(sys.argv[1:])
