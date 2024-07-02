#we will be implementing tree ds so we start again
# today we created this two different class objects
#33:59

class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None   #ref variable which will point our root node at first
        # self.val = []    #we will not use a list as it will use another ds to create and hence will be much complex later on

    def insert(self, data):
        self.root= self.rinsert(self.root, data)
    
    def rinsert(self, root, data): #recursion function started still not able to get it
        if root is None:
            return Node(data)

        if data < root.item:
            root.left = self.rinsert(root.left, data)
            print("left")

        elif data > root.item:
            root.right = self.rinsert(root.right, data)
            print("right")

        return root

    def search(self, data):
        return self.rsearch(self.root, data)
    
    def rsearch(self, root, data):
        if root is None or root.item==data:
            return root
        if data < root.item:
            return self.rsearch(root.left, data)
        else:
            return self.rsearch(root.right, data)




new = BinarySearchTree()

print(new.insert(2))
print(new.insert(1.1))
print(new.insert(39))
print(new.insert(1))
print(new.insert(45))
print(new.search(39))