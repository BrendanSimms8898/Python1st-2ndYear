def main():
	print("Enter a name and number, or a name and ? to query (!! to exit)")
	inp = input()
	d = {}
	while inp != "!!":
		inp = inp.strip().split()
		if inp[1] == "?":
			if inp[0] in d:
				print(str(inp[0]) + " has number " + str(d[inp[0]]))
			else:
				print("Sorry, there is no " + str(inp[0]))
		else:
			d[inp[0]] = int(inp[1])
		inp = input()
	print("Bye")

if __name__ == '__main__':
	main()

#A program to manage phone numbers. A user enters commands a line at a time. There are three commands:
#1. !! (two exclamation marks) exits the program
#2. name number associates a number to a name. Note that the name cannot have spaces and if a second number is added to a name, it overwrites the first.
#3. name ? gives the number for that name