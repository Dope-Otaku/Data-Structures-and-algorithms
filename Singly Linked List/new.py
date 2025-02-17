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





#drivers code
myList = SLL()

print(myList.isEmpty())