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
        node = Node(None, None, item)
        temp = self.start
        p
        if self.is_empty():
            self.start = node
            print(f"added the item: {item} in node stored at {node} at first as node was empty!")
        else:
            while temp is not None:
                tempNode = temp.next
                tempNode.prev = node
                print(f"added the item: {item} in node stored at {node} but this is betweeen an earlier node!")
            
    

n = dll()
print(n)
print(n.insertAtFirst(1))
print(n.is_empty())