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
            newNode.right = self.root.right
            newNode.left = self.root.left
            self.root.left, self.root.right = None, None
            self.root = newNode
            return f"changed the root node to {data}"
        self.root = newNode
        return f"inserted root node {data}"

    

    def insertatleft(self, data):
        if self.root.left == None:
            newNode = Node(item=data)
            self.root.left = newNode

    def insertatright(self, data):
        if self.root.right == None:
            newNode = Node(item=data)
            self.root.right = newNode




# driver code

myList = BST()
print(myList.insertatroot(data=1))
print(myList.isEmpty())
print(myList.insertatroot(data=2))
