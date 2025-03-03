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

    def insert(self, data):
        self.root = self.rinsert(self.root, data)

    def rinsert(self, root, data):
        if self.root is None:
            return Node(item=data)
        if data < root.item:
            root.left =  self.rinsert(root.left, data)
        elif data > root.item:
            root.right = self.rinsert(root.right, data)
        return root

    def traversing_preorder(self):
        temp = self.root
        if temp is None:
            return temp.item
        else:
            while  temp is not None:
                print(temp.item)
                temp = temp.left
                pass



# driver code

myList = BST()
print(myList.insert(100))
print(myList.insert(10))
print(myList.insert(101))
print(myList.insert(20))
print(myList.isEmpty())
