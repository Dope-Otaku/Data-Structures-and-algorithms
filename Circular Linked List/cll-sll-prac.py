'''
in this we will practise circular Doubly linked list
'''
class Node:
    def __init__(self, data=None, next= None):

        self.data = data
        self.next = next

class CLL:
    def __init__(self, start=None):
        self.start = start

    def __iter__(self):
        return CLLIterator(self.start)

    def isEmpty(self):
        return self.start == None

    def travserse(self):
        temp = self.start
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next

    def insertFront(self, item):
        newNode = Node(data = item)
        # if not self.isEmpty():
        #     self.start = newNode
        # self.start = newNode


        # the logic needs to be imiplemented new
        if self.start == None:
            self.start = newNode

    def insertLast(self, item):
        newNode = Node(data = item, next= self.start)
        temp = self.start
        # if self.isEmpty():
        #     self.start = newNode
        while temp is not None:
            if temp.next == self.start:
                temp.next = newNode
                print("hi")
            temp = temp.next



class CLLIterator:
    def __init__(self, start):
        self.current = start

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
print(myList.travserse())
print(myList.insertLast(3))



# iterator

for x in myList:
    print(x, end=' ')
