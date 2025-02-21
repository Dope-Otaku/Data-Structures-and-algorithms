'''
in this we will practise circular singly linked list
'''
class Node:
    def __init__(self, prev=None, data=None, next= None):
        self.prev = prev
        self.data = data
        self.next = next

class CLL:
    def __init__(self, start=None):
        self.start = start

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






# drivers code

myList = CLL()

print(myList.isEmpty())
print(myList.insertFront(1))
print(myList.insertFront(2))
print(myList.travserse())
