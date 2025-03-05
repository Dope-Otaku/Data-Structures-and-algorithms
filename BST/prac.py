class Node:
    def __init__(self, left=None, item=None, right=None):
        self.left = left
        self.item = item
        self.right = right

    
class BST:

    def __init__(self, root=None):
        self.root = root
        self.count = 0

    def isEmpty(self):
        return self.root == None

    def insert(self, data):
        self.root = self.rinsert(self.root, data)
    
    def rinsert(self, root, data):
        if root is None:
            return Node(item=data)
        if data < root.item:
            root.left = self.rinsert(root.left, data)
        elif data > root.item:
            root.right = self.rinsert(root.right, data)
        return root
        
    def size(self):
        return len(self.inorder())


    def search(self, data):
        return self.rsearch(self.root, data)

    def rsearch(self, root, data):
        if root is None or root.item == data:
            return root
        if data < root.item:
            return self.rsearch(root.left, data)
        else:
            return self.rsearch(root.right, data)

    def inorder(self):
        results = []
        self.rinorder(self.root, results)
        return results

    def rinorder(self, root, results):
        if root:
            self.rinorder(root.left, results)
            results.append(root.item)
            self.rinorder(root.right, results)

    def max_val(self, temp):
        curr = temp
        while curr.right is not None:
            curr = curr.right
        return curr.item


    def delete(self, data):
        self.root = self.rdelete(self.root, data)

    def rdelete(self, root, data):
        if root is None:
            return root
        if data > root.item:
            root.right = self.rdelete(root.right, data)
        elif data < root.item:
            root.left = self.rdelete(root.left, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item = self.max_val(root.right)
            root.right = self.rdelete(root.right, root.item)
        return root

#driver code

myList = BST()
print(myList.isEmpty())
print(myList.insert(100))
print(myList.insert(10))
print(myList.insert(101))
print(myList.insert(20))
print(myList.insert(45))
print(myList.insert(33))
print(myList.insert(9))
print(myList.insert(2))
print(myList.insert(25))
print(myList.insert(26))
print(myList.insert(34))
print(myList.insert(88))
print(myList.insert(200))
print(myList.search(84))
print(myList.size())
print(myList.inorder())
print(myList.delete(33))
print(myList.inorder())
print(myList.size())
