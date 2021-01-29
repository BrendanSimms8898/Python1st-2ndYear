import sys

a = {line.strip() for line in open(sys.argv[1], "r")}
b = {line.strip() for line in open(sys.argv[2], "r")}
bad = [n for n in a&b]
#bad = " ".join(set(a&b)).split()
bad.sort()
for i in range(1, len(bad)+1):
    print(str(i) + ". " + str(bad[i-1]))

    #Program to check if name apears in two lists of a text file

    #example of lists: students.txt
    #Johnny be good
    #Boney Vox
    #The Edge
    #John Lennon
    #Shakira
    #Bob Dylan
    #James Brown

    #delinquents.txt
    #Baddie ThreeShoes
    #Attila the Hun
    #Boney Vox
    #Agolf Hitler   
    #Bob Dylan
    #Shakira
