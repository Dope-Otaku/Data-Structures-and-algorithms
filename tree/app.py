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

    def insert_at_node(self, data):
        #self.root.item this is directly pointing atat our root node objects 
        # print(self.root.item)
        start = self.root
        if start.item > data:
            if start.left == None:
                node = Node(item=data)
                start.left = node
                return f"inserted on left side since it({data}<{start.item}) was smaller"
            else: #from this else point onards it will start forming a tree
                print(f"hello {start.left.item} | {start.right.item}") #just for checking my values
                if start.left.item > data:
                    node = Node(item=data)
                    start.left.left = node
                    return f"inserted on right side since it was smaller" 
        elif start.item < data:
            if start.right == None:
                node = Node(item=data)
                start.right = node
                return f"inserted on right side since it({data}>{start.item}) was bigger"
            else: #from this else point onards it will start forming a tree
                print(f"hello {start.left.item} | {start.right.item}") #just for checking my values
                if start.left.item < data:
                    node = Node(item=data)
                    start.left.right = node
                    return f"inserted on right side since it was bigger"
        else:
            return f"Duplicates are not allowed!"
            #they are not able to enter this block
        # self.root = node
        # node = Node(item=item)
        # #let us say we need to insert this {70,10,25,40,50}
        # if node.item == item:
        #     return f"duplicates are not allowed"
        # else:
        #     if node.item > item:
        #         node.left = node
        #     else:
        #         node.right = node

        # return f"{node.item} at root node"

new = BinarySearchTree()
print(new.inser_atfirst(70))
print(new.insert_at_node(10))
print(new.insert_at_node(80))
print(new.insert_at_node(40))
print(new.insert_at_node(50))
print(new.insert_at_node(60))
print(new.insert_at_node(15))