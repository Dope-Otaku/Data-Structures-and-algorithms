'''
in this we will practise circular Doubly linked list
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

    def insertLast(self, item): #this function is obsolete
        newNode = Node(data = item, next= self.last)
        temp = self.last
        # if self.isEmpty():
        #     self.last = newNode
        while temp is not None:
            if temp.next == self.last:
                temp.next = newNode
                print("hi")
            temp = temp.next



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
print(myList.isEmpty())
print(myList.travserse())
# print(myList.insertLast(3))



# iterator

# for x in myList:
#     print(x, end=' ')
