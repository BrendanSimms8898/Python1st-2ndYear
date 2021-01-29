#function which takes a linked list of integers as an argument and counts the number of even elements in the list

def even_count(lst):
	nums = 0
	while not lst.is_empty():
		n = lst.remove()
		if n % 2 == 0:
			nums += 1
	return nums

#Code to test provided by lecturer

def main():
    # Read each set
    line = sys.stdin.readline()
    items = line.strip().split()
    nums = [int(item) for item in items]
    
    ll = LinkedList()
    
    for num in nums:
        ll.add(num)
    
    print(even_count(ll))

if __name__ == "__main__":
    main()
