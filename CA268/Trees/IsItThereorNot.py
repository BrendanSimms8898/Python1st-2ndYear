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
#New function added to LinkedList Class which returns true if its argument is contained in the list
    def contains(self,e):
        ptr=self.head
        contain=False
        while ptr!=None:
            if e==ptr.item:
                contain=True
            ptr=ptr.next
        return contain

    #code to test provided by lecturer:

def main():
    # Read each line
    line = sys.stdin.readline()
    items = line.strip().split()
    
    ll = LinkedList()
    problem = False
    if ll.contains(items[0]):
        print("An empty list should not match anything")
        problem = True
    
    else:
        for item in items:
            if ll.contains(item):
                print(item + " detected before being added.")
                problem = True
            ll.add(item)
            
        # Now every item in the items should be in the list.
        for item in items:
            if not ll.contains(item): # item should not be contained
                print(item + " not found in list.")
                problem = True

    if not problem:
        # check that the list still contains all the items
        while not ll.is_empty() and len(items) > 0:
            if ll.remove() != items.pop():
                print("List has been modified")
                problem = true
                break
        
        if not problem:
            if (not ll.is_empty()) or len(items) != 0:
                print("the list size is wrong");
                problem = True
                
    if problem:
        print("More work needed!")
    else:
        print("all ok!")

if __name__ == "__main__":
    main()
    
