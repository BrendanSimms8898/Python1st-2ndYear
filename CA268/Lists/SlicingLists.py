def get_sliced_lists(a):
    l = []
    l.append(a[:-1])
    l.append(a[1:-1])
    l.append(a[::-1])
    return l

#Test Code provided by lecturer:
#from numbers import get_sliced_lists

#def main():
    # read the list from stdin
    #nums = []
    #num = int(input())
    #while num != -1:
        #nums.append(num)
        #num = int(input())
        
    # call the student's function with the list of numbers and ...
    #lists = get_sliced_lists(nums)
    # ... print the result
    #for lst in lists:
        #print(lst)

#if __name__ == "__main__":
    #main()
    
#Creates Three lists:
#1. A list including all but the last element
#2. A list including all but the first and last elements
#3. A reversed list (created using slicing)
