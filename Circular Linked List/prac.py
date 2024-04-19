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

    def insertatFirst(self, data): #no traversing
        #node created at first
        node = Node(data)
        #if list is empty 
        if self.isEmpty():
            node.next = node #make a pointer to itself
            self.last = node #make a poibter to self.last
            print(f"list was empty so added at first directly at {node}")
        else:
            #if list is not empty
            node.next = self.last.next 
            self.last.next = node
            print(f"list was not empty so added  at {node}")

    def insertAtlast(self, data): #no traversing
        #node created
        node = Node(data)
        # if list is empty
        if self.isEmpty():
            node.next = node
            self.last = node
            print(f"list was empty so added at last directly at {node}")
        #if it is not empty
        else:
            #first add a pointer of first node to new node from the last node
            last = self.last.next
            node.next = last
            #now our new node has a connection with first node now we want it to be connected with last node
            last = node
            #now we will move the start pointer(last) to the new node
            self.last = node
            print(f"list was not empty so added  at {node}")

    def search(self, data): #caution runs infinitely so make sure to stop it soon after it is done
        temp = self.last
        while temp.next is not None:
            if self.isEmpty():
                return f"the list is empty"
            if(data==temp.item):
                return f"item:{data} found at {temp}"
            temp = temp.next
            break
            
new = CLL()

print(new)
print(new.insertatFirst(9))
print(new.insertatFirst(10))
print(new.insertAtlast(11))
print(new.search(11))
print(new.isEmpty())