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

    def insertatroot(self, data):
        newNode = Node(item=data)
        if not self.isEmpty():
            return "hek"
        self.root = newNode
        return f"inserted root node"






# driver code

myList = BST()
print(myList.insertatroot(data=1))
print(myList.isEmpty())