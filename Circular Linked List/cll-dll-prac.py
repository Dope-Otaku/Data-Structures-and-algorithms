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
    def deleteFront(self): #need fixing value not getting deleted!
        temp = self.start
        while temp is not None:
            self.start.prev.next = temp.next
            temp.next.prev = self.start.prev
            self.start = temp
            break
        return


class CIterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self.current

    def __next__(self):
        if not self.current:
            raise StopIteration
        tempData = self.current.data
        count =1 
        # if self.current 





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
print(myList.deleteFront())
print(myList.traverse())