'''
in this we will practise circular Doubly linked list and imp point to remember we will start
traversing from last which will decrease the time to traverse last node and not start node

note = the first node prev links to last node

'''

class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class CLL:
    def __init__(self, start=None):
        self.start = start

    def __iter__(self):
        return CIterator(self.start)

    def isEmpty(self):
        return self.start == None

    def traverse(self): #basically printing all values
        temp = self.start
        while temp is not None:
            print(temp.data, end =" ")
            if temp.next == self.start:
                break
            temp = temp.next

    def search(self, item):
        temp = self.start
        while temp is not None:
            if temp.data == item:
                return f"found item:{item} at {temp}"
            elif temp.data == item and temp.next == self.start:
                return f"found item:{item} at {temp}"
            temp = temp.next
            if temp.data != item and temp.next == self.start:
                return f"Item:{item}, not available in list!"
        return f"List Empty!"

    def insertFront(self, item):
        newNode = Node(data = item)
        if self.start == None:
            self.start = newNode        
        elif self.start.next == None:
            newNode.next = self.start
            self.start.next = newNode
            newNode.prev = self.start
            self.start = newNode
        else:
            newNode.next = self.start
            newNode.prev = self.start.prev
            self.start.prev = newNode
            self.start = newNode
            newNode.prev.next = newNode
        
    def insertLast(self, item):
        newNode =Node(data = item)
        if self.start == None:
            self.start = newNode
        newNode.next = self.start
        self.start.prev.next = newNode
        newNode.prev = self.start.prev
        self.start.prev = newNode

    def insertAfter(self, after, item):
        newNode =Node(data = item)
        if self.start == None:
            self.insertFront(item)
        temp = self.start
        while temp is not None:
            if temp.data == after:
                newNode.prev = temp
                newNode.next = temp.next
                temp.next.prev = newNode
                temp.next = newNode
                break
            elif temp.data == after and temp.next == self.start:
                self.insertLast(item)

            temp = temp.next
        
    # learned a new thing we can do manual memory managemnet just for learning purpose {del (variable name)} :- del temp
    def deleteFront(self): 
        if not self.isEmpty():
            self.start.prev.next = self.start.next
            self.start.next.prev = self.start.prev
            self.start = self.start.next

    def deleteLast(self):
        if not self.isEmpty():
            self.start.prev.prev.next = self.start
            self.start.prev = self.start.prev.prev

    def deleteAfter(self, after):
        temp = self.start
        while temp is not None:
            if temp.data == after:
                if temp.data == after and temp.next.next == None:
                    self.deleteLast()
                    # print("last loop mai jarah")
                temp.next.next.prev = temp
                temp.next = temp.next.next
                # print("last nahi hai")
                break
                
            temp = temp.next
        # return f"fucked out of loop!"


class CIterator:
    def __init__(self, start):
        self.current = start
        self.temp = start
        self.count = 0

    def __iter__(self):
        return self.current

    def __next__(self):
        if not self.current:
            raise StopIteration
        tempData = self.current.data
        if self.current == self.temp and self.count == 1:
            raise StopIteration
        else:
            self.count = 1
        self.current = self.current.next
        return tempData





# driver's code

myList = CLL()

# print(myList.insertFront(5))
# print(myList.insertFront(4))
print(myList.insertFront(3))
print(myList.insertFront(2))
print(myList.insertFront(1))
print(myList.insertLast(4))
print(myList.insertLast(5))
print(myList.insertAfter(5, 5.5))
print(myList.search(0))
print(myList.traverse())
# print(myList.deleteFront())
# print(myList.deleteLast())
print(myList.deleteAfter(5))
print(myList.traverse())

for x in myList:
    print(x, end=" ")