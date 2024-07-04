#we will be implementing tree ds so we start again
# today we created this two different class objects
#33:59
#need to watch recursion vid again ig
# ok so i have a slight idea of how does this recursion takes place and also  
# so first we normally insert it and then we call a another function
#and then when it inserts the third value it simply bypasses the prev vlues and just saved in the new left or righ memmory pf the tree

#now the traversing part is working very well
class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BinarySearchTree: #name can be anything
    def __init__(self):
        self.root = None   #ref variable which will point our root node at first
        # self.val = []    #we will not use a list as it will use another ds to create and hence will be much complex later on

    def insert(self, data):
        self.root= self.rinsert(self.root, data)
    
    def rinsert(self, root, data): #recursion function started still not able to get it
        if root is None:
            return Node(data)

        if data < root.item:
            root.left = self.rinsert(root.left, data) #this paert specifically
            print("left")

        elif data > root.item:
            root.right = self.rinsert(root.right, data)
            print("right")

        return root


    # def insert(self, data):
    #     self.root = self.rinsert(self.root, data)

    # def rinsert(self, root, data):
    #     if root is None:
    #         return Node(data)
    #     elif data < root.item:
    #         root.left = self.rinsert(root.left, data)

    #     elif data > root.item:
    #         root.right = self.rinsert(root.right, data)

    #     return root

#need to one again learn this
    # def search(self, data):
    #     return self.rsearch(self.root, data) #again this recursion
    
    # def rsearch(self, root, data):
    #     if root is None or root.item==data:
    #         return root
    #     if data < root.item:
    #         return self.rsearch(root.left, data)
    #     else:
    #         return self.rsearch(root.right, data)


    def search(self, data):
        return self.rsearch(self.root, data)

    def rsearch(self, root, data):
        if root is None or root.item == data:
            return root
        if data < root.item:
            return self.rinsert(root.left, data)
        else:
            return self.rinsert(root.right, data)

    def inorder(self):
        result = []
        self.rinorder(self.root, result)
        return result
    
    def rinorder(self, root, result):
        if root:
            self.rinorder(root.left, result)
            result.append(root.item)

            self.rinorder(root.right, result)
            # result.append(root.item)
    
    def preorder(self):
        result = []
        self.rpreorder(self.root, result)
        return result


    def rpreorder(self, root, result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left, result)
            self.rpreorder(root.right, result)

    def postorder(self):
        result = []
        self.rpostorder(self.root, result)
        return result


    def rpostorder(self, root, result):
        if root:
            self.rpostorder(root.left, result)
            self.rpostorder(root.right, result)
            result.append(root.item)

    def minValue_full(self):
        res = self.inorder()[0]
        # ans = res[0]
        # return ans
        return res
    
    def maxValue_full(self):
        res = self.inorder()
        ans = res[len(res)-1]
        return ans

    def delete(self, data):
        return self.rdelete(self.root, data)

    def rdelete(self, root, data):
        if root is None:
            return None
        if data < root.item:
            root.left = self.rdelete(root.left, data)
            if root.left is None or root.right is None:
                root.left = self.rdelete(root.left, data)



new = BinarySearchTree()

print(new.insert(50))
print(new.insert(30))
print(new.insert(10))
print(new.insert(40))
print(new.insert(80))
print(new.insert(70))
print(new.insert(100))
print(new.search(40))
print(new.inorder())
print(new.preorder())
print(new.postorder())
print(new.minValue())
print(new.maxValue())