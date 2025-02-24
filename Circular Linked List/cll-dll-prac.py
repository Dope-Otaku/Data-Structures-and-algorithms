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


    def isEmpty(self):
        return self.start == None

    def traverse(self): #basically printing all values
        if not self.isEmpty():
            temp = self.start
            while temp is not None:
                if temp.next == self.start:
                    print(temp.data)
                    break
                temp = temp.next


    def insertFront(self, item):
        newNode = Node(data = item)
        if not self.isEmpty():
            newNode.next = self.start
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            newNode.prev = temp.next
            temp.next.next = newNode
            self.start = newNode
        self.start = newNode


# driver's code

myList = CLL()

print(myList.insertFront(5))
print(myList.insertFront(4))
print(myList.insertFront(3))
print(myList.insertFront(2))
print(myList.insertFront(1))
print(myList.traverse())