class Node:
    def __init__(self, left=None, item=None, right=None):
        self.left = left
        self.item = item
        self.right = right



class BST:
    def __init__(self, root=None):
        self.root = root

    def isEmpty(self):
        return self.root == None

    def insertion(self, data):
        newNode = Node(item=data)
        if self.root == None:
            self.root = newNode
        




# driver code

myList = BST()
print(myList.insertion(1))
print(myList.isEmpty())
