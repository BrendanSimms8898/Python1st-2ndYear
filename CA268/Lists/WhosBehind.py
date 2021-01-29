import sys
class Node:
    def __init__(self, item, nxt):
        self.item = item
        self.next = nxt

# Note, these are methods "A method is a function that is stored as a class attribute"
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None

    def count(self):
        ptr= self.head
        count=0
        while ptr!= None:
            count+=1
            ptr=ptr.next
        return count

    def contains(self,e):
        ptr=self.head
        contain=False
        while ptr!=None:
            if e==ptr.item:
                contain=True
            ptr=ptr.next
        return contain
#New function added to LinkedList Class which takes as parameter an item and returns the item that occurs after it in the linked list. If no such item exists, then return None.
    def after(self,e):
        ptr=self.head
        while ptr!=None:
            if ptr.item==e:
                return ptr.next.item
            ptr=ptr.next
        return None

 def main():
    # Read each set
    line = sys.stdin.readline()
    items = line.strip().split()
    
    tests = [] # list of the results of the tests
    
    ll = LinkedList()

    # Check that it works for an empty list    
    tests.append(ll.after("") == None)  # Each test should be True

    # Check that the item doesn't exist before it is added    
    for item in items:
        tests.append(ll.after(item) == None)
        ll.add(item)
    
    items.reverse()
    for i in range(len(items) - 1):
        # print(ll.after(items[i]), items[i+1])
        tests.append(ll.after(items[i]) == items[i+1])
        
    print("All Good" if all(tests) else str(tests))

if __name__ == "__main__":
    main()
