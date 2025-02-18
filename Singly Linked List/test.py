class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SLL():
    def __init__(self, start=None):
        self.start = start

    def isEmpty(self):
        return self.start==None

    def iterator(self):
        return SLLIterator(self.start)
    
    def printAll(self):
        temp = self.start
        while temp is not None:
            print(temp)
            temp = temp.next

    def insertFront(self, item):
        newNode = Node(item)
        if not self.isEmpty():
            newNode.next = self.start
        self.start = newNode

    def insertLast(self, item):
        newNode = Node(item)
        if self.isEmpty():
            self.start = newNode
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode
        
    def insertItem(self, item , data):
        newNode = Node(item)
        if self.start.data == data:
            self.start.next = newNode
            return 
        if not self.isEmpty():
            temp = self.start
            while temp is not None:
                if temp.data == data:
                    newNode.next = temp.next
                    temp.next = newNode
                    break
                temp = temp.next

    def search(self, item):
        if not self.isEmpty():
            temp = self.start
            while temp is not None:
                if temp.data == item:
                    return f"item found"
                temp =temp.next
        else:
            return f"list empty"

    def deleteFirst(self):
        if self.start == None:
            return -1
        elif self.start.next == None:
            self.start = None
        else:
            temp = self.start
            self.start = temp.next

    def deleteLast(self):
        if self.start == None:
            return -1
        elif self.start.next == None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = None

    def deleteItem(self, item):
        if not self.isEmpty():
            temp = self.start
            while temp is not None:
                if temp.next.data == item:
                    temp.next = temp.next.next
                    break
                temp = temp.next
                    
class SLLIterator():
    def __init__(self):
        self.current = current

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        tempData = self.current.data
        self.current = self.current.next





#driver code

myList = SLL()

print(myList.insertFront(1))
