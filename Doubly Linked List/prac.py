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
        if self.start is not None:
            return f"List is empty"

    

n = dll()
print(n)
print(n.is_empty())