#doubly linked list

class dll:
    def __init__(self, start=None):
        self.start = start

class Node:
    def __init__(self, prev=None, next=None, item=None):
        self.prev = prev
        self.next = next
        self.item = item

n = Node()
print(n)
