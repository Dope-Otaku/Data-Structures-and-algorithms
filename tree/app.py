#we will be implementing tree ds so we start again

class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class Tree:
    def __init__(self, root=None):
        self.root = root   #ref variable which will point our root node at first
        self.val = []

    def printA(self):
        self.val.append(1)
        return f"{self.val}"
    
    def insert_at_root(self, item):
        node = Node(item)
        self.root = node
        return f"{node.item} at root node"

new = Tree()
print(new.printA())
print(new.insert_at_root(2))