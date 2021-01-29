class Node:
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    def __init__(self, lst = None):
        self.root = None
        if lst != None:
            for item in lst:
                self.add(item)

    def add(self, item):
        if self.root == None:
            self.root = Node(item, None, None)
        else:
            lst = []
            child_tree = self.root
            while child_tree != None:
                lst.append(child_tree.item)
                parent = child_tree
                if item < child_tree.item:
                    child_tree = child_tree.left
                else:
                    child_tree = child_tree.right
            if item < parent.item:
                parent.left = Node(item, None, None)
            else:
                parent.right = Node(item, None, None)
            lst.reverse()
            return lst

#Added the add() method so that it returns a list of the items in the path from the node which was just added to the root. For example, if a 1 was added to the following binary search tree:
#               8
#       5                 10
#  3       6          9
#then it would end up in the leftmost position and the path to the root would be 3, 5, 8 so it should return the list [3, 5, 8]

