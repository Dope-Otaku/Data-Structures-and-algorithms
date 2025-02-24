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