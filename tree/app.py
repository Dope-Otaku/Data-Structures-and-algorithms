#we will be implementing tree ds so we start again
# today we created this two different class objects
#33:59
#need to watch recursion vid again ig
class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BinarySearchTree: #name can be anything
    def __init__(self):
        self.root = None   #ref variable which will point our root node at first
        # self.val = []    #we will not use a list as it will use another ds to create and hence will be much complex later on

    # def insert(self, data):
    #     self.root= self.rinsert(self.root, data)
    
    # def rinsert(self, root, data): #recursion function started still not able to get it
    #     if root is None:
    #         return Node(data)

    #     if data < root.item:
    #         root.left = self.rinsert(root.left, data) #this paert specifically
    #         print("left")

    #     elif data > root.item:
    #         root.right = self.rinsert(root.right, data)
    #         print("right")

    #     return root


    def insert(self, data):
        self.root = self.rinsert(self.root, data)

    def rinsert(self, root, data):
        if root is None:
            return Node(data)
        elif data < root.item:
            root.left = self.rinsert(root.left, data)

        elif data > root.item:
            root.right = self.rinsert(root.right, data)

        return root

#need to one again learn this
    def search(self, data):
        return self.rsearch(self.root, data) #again this recursion
    
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