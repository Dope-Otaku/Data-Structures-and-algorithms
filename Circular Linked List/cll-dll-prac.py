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
        newNode = Node(data = item, next = self.start)
        if not self.isEmpty():
            self.start = newNode
        self.start = newNode

    def insertLast(self, item):
        pass



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
# print(myList.travserse())


# iterator

for x in myList:
    print(x, end=' ')
