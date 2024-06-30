#we will be implementing tree ds so we start again
# today we created this two different class objects

class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root   #ref variable which will point our root node at first
        # self.val = []    #we will not use a list as it will use another ds to create and hence will be much complex later on

    # def printA(self):
    #     self.val.append(1)
    #     return f"{self.val}"
    
    def inser_atfirst(self, data):
        node = Node(item=data) #initiated a new node
        self.root = node
        return f"data: {data} inserted at root node!"

    def insert_at_node(self, item):
        self.root = node
        node = Node(item=item)
        #let us say we need to insert this {70,10,25,40,50}
        if node.item == item:
            return f"duplicates are not allowed"
        else:
            if node.item > item:
                node.left = node
            else:
                node.right = node

        return f"{node.item} at root node"

new = BinarySearchTree()
print(new.inser_atfirst(2))