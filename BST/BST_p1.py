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
        else:
            temp = self.root
            while temp is not None:
                if self.root.item > data:
                    if self.root.item == None:
                        self.root.left = newNode
                    else:
                        temp = self.root.left
                        
                    if self.root.item
                elif self.root.item < data:
                    self.root.right = newNode
            




# driver code

myList = BST()
print(myList.insertion(1))
print(myList.isEmpty())
