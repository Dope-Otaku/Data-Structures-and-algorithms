class Node:
    def __init__(self, prev=None, next=None, data=None):
        self.prev = prev
        self.next = next
        self.data = data




class DLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def printAll(self):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                print(temp.data, end = ' ')
                temp = temp.next



    def insert_first(self, data):
        newNode = Node(None,self.start, data)
        # print(newNode.data)
        if not self.is_empty():
            self.start.prev = newNode
            print(f"added a new list with{data}")
        self.start = newNode
        print(f"added the list with{data}")

    def insert_last(self, data):
        newNode = Node(data = data)
        if self.start == None:
            self.start = newNode
        
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        newNode.prev = temp
        temp.next = newNode
        print(f"added in the last list {data}")
            
        




#driver code

myList = DLL()

print(myList.is_empty())
print(myList.insert_first(4))
print(myList.insert_first(3))
print(myList.insert_first(2))
print(myList.insert_first(1))
print(myList.insert_last(5))
print(myList.printAll())

