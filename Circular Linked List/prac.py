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
            node.next = self.last.next
            #now our new node has a connection with first node now we want it to be connected with last node
            self.last.next = node
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
    
    def printlist(self):
        if not self.isEmpty():
            # return f"List is empty."
            temp = self.last.next
            # print(temp.item)
            
            while temp is not self.last:
                print(temp.item, end=" ")
                temp = temp.next
            
            # Print the last item
            print(temp.item)
            
    def insertAfter(self, temp, data):
        if temp is not None:
            node = Node(data, temp.next)
            temp.next = node
            if temp == self.last:
                self.last=node
            
    def delete_first(self):
        if not self.isEmpty():
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next
                print(self.last.next.item) # Print the item of the node being deleted
            return f"successfully deleted from the list" 
    
    def delete_last(self):
        if not self.isEmpty():
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next!= self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp
    
    def delete_after(self, item):
        pass


    
new = CLL()

print(new)
print(new.insertatFirst(9))
print(new.insertatFirst(10))
print(new.insertatFirst(12))
print(new.insertAtlast(11))
print(new.search(11))
print(new.isEmpty())
print(new.printlist())
print(new.delete_first())
print(new.printlist())
