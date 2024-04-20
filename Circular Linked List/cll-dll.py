#circular doubly linked list

class Node:
    def __init__(self, item=None, prev=None, next=None):
        self.item = item
        self.prev= prev
        self.next = next

class CLL:
    def __init__(self, start=None):
        self.start = start

    def isEmpty(self):
        return self.start==None
    
new = CLL()
print(new.isEmpty())