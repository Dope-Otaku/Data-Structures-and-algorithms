'''
in this we will practise circular Doubly linked list and imp point to remember we will start
traversing from last which will decrease the time to traverse last node and not start node
'''
class Node:
    def __init__(self, data=None, next= None):

        self.data = data
        self.next = next

class CLL:
    def __init__(self, last=None):
        self.last = last

    def __iter__(self):
        return CLLIterator(self.last)

    def isEmpty(self):
        return self.last == None

    def travserse(self):
        temp = self.last
        while temp is not None:
            print(temp.data, end=' ')
            if temp.next == self.last:
                break
            temp = temp.next

    def insertFront(self, item):
        newNode = Node(data = item)
        if self.isEmpty():
            self.last = newNode
        elif self.last.next == None:
            newNode.next = self.last
            self.last.next = newNode
        else:
            newNode.next = self.last.next
            self.last.next = newNode

    def insertLast(self, item): 
        newNode = Node(data = item)
        if self.last == None:
            self.last = newNode
        else:
            newNode.next = self.last.next
            self.last.next = newNode
            self.last = newNode
        



class CLLIterator:
    def __init__(self, last):
        self.current = last

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        tempData = self.current.data
        self.current = self.current.next
        return tempData



# drivers code

myList = CLL()

print(myList.isEmpty())
print(myList.insertFront(1))
print(myList.insertFront(2))
print(myList.insertFront(3))
print(myList.insertFront(4))
print(myList.insertLast(5))
print(myList.insertLast(6))
# print(myList.isEmpty())
print(myList.travserse())



# iterator

# for x in myList:
#     print(x, end=' ')
