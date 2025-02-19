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


    def insert_first(self, data):
        newNode = Node(None,self.start, data)
        # print(newNode.data)
        if self.is_empty():
            self.start = newNode
        self.start.prev = newNode



#driver code

myList = DLL()

print(myList.is_empty())
print(myList.insert_first(1))

