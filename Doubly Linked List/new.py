class Node:
    def __init__(self, prev=None, next=None, data=None):
        self.prev = prev
        self.next = next
        self.data = data




class DLL:
    def __init__(self):
        self.start = None

    def is_empty(self):
        return self.start == None






#driver code

myList = DLL()

print(myList.is_empty())