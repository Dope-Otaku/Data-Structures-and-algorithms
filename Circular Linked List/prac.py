#circular linked list

class Node:
    def __init__(self, item=None , next=None):
        self.item = item
        self.next = next
class CLL:
    def __init__(self, start=None):
        self.start = start

    def isEmpty(self):
        if self.start == None:
            return True
        return False
    
    def listPrint(self):
        pass

    def insertatFirst(self, data):
        #node created at first
        node = Node(data)
        #if list is not empty 
        if not self.isEmpty():
            temp = self.start
            temp.next = node
            node = temp.next.next
            print("a")

            
        #if list is empty
        self.start = node
        return f"added succesfully"



new = CLL()

print(new)
print(new.insertatFirst(9))
print(new.insertatFirst(10))
print(new.isEmpty())