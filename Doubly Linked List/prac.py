#doubly linked list

class Node:
    def __init__(self, prev=None, next=None, item=None):
        self.prev = prev
        self.next = next
        self.item = item

class dll:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        if self.start is None:
            return f"List is empty"
        else:
            return f"List is not Empty!"
        
    def insertAtFirst(self, item):
        node = Node(None, self.start, item)

        if not self.is_empty():
            self.start.prev = node
            print(f"the list was not empty and hence added")
        self.start = node
        print(f"list was empty and hence added the node {node}")           
    

n = dll()
print(n)
print(n.insertAtFirst(1))
print(n.is_empty())
print(n.insertAtFirst(2))
