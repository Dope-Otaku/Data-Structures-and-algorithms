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

    def size(self):
        return self.count

    def insert(self, data):
        self.root = self.rinsert(self.root, data)
        self.count += 1

    def rinsert(self, root, data):
        if root is None:
            return Node(item=data)
        if data < root.item:
            root.left =  self.rinsert(root.left, data)
        elif data > root.item:
            root.right = self.rinsert(root.right, data)
        return root

    def search(self, data):
        return self.rsearch(self.root, data)

    def rsearch(self, root, data):
        if root is None or root.item == data:
            return root
        if data < root.item:
            return self.rsearch(root.left, data)
        else:
            return self.rsearch(root.right, data)

    def inorder(self): #inorder -> tl < root < tr
        reults = []
        self.rinorder(self.root, reults)
        return reults

    def rinorder(self, root, reults):
        if root:
            self.rinorder(root.left, reults)
            reults.append(root.item)
            self.rinorder(root.right, reults)

    def preorder(self):#preorder -> root < tl < tr 
        results = []
        self.rpreorder(self.root, results)
        return results

    def rpreorder(self, root, results):
        if root:
            results.append(root.item)
            self.rpreorder(root.left, results)
            self.rpreorder(root.right, results)

    def postorder(self):#postorder -> tl < tr < root
        results = []
        self.rpostorder(self.root, results)
        return results

    def rpostorder(self, root, results): 
        if root:
            self.rpostorder(root.left, results)
            self.rpostorder(root.right, results)
            results.append(root.item)

    def delete(self, data):
        pass
   

# driver code

myList = BST()
print(myList.insert(100))
print(myList.insert(10))
print(myList.insert(101))
print(myList.insert(20))
print(myList.isEmpty())
print(myList.search(20))
print(myList.inorder())
print(myList.preorder())
print(myList.postorder())
print(myList.size())
