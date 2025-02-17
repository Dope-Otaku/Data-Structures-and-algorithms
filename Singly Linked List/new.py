# linkeed list practise

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SLL:
    def __init__(self, start=None):
        self.start = start

    def isEmpty(self):
        return self.start == None

    # new peek view function added for debugging
    def currentPointer(self):
        if self.start is None:
            return f"the list is empty"
        else:
            return self.start.data

    def insertFront(self, item):

        #new node creation
        newNode = Node(item, self.start)
        self.start = newNode
        return f"New List created with {item}"






#drivers code
myList = SLL()

print(myList.isEmpty())
print(myList.insertFront(1))
print(myList.insertFront(2))
print(myList.currentPointer())