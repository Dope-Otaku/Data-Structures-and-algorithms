#circular linked list

class Node:
    def __init__(self, item=None , next=None):
        self.item = item
        self.next = next
class CLL:
    def __init__(self, last=None):
        self.last = last

    def isEmpty(self):
        if self.last == None:
            return True
        return False
    
    def listPrint(self):
        pass

    def insertatFirst(self, data):
        #node created at first
        node = Node(data)
        #if list is empty 
        if self.isEmpty():
            node.next = node
            self.last = node
            print(f"list was empty so added at first directky at {node}")
        else:
            node.next = self.last.next
            self.last.next = node
            print(f"list was not empty so added  at {node}")



new = CLL()

print(new)
print(new.insertatFirst(9))
print(new.insertatFirst(10))
print(new.isEmpty())