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






# drivers code

myList = CLL()

print(myList.isEmpty())