class Node:
    def __init__(self, prev=None, next=None, data=None):
        self.prev = prev
        self.next = next
        self.data = data




class DLL:
    def __init__(self, start=None):
        self.start = start
    
    def __iter__(self):
        return DLLIterator(self.start)

    def is_empty(self):
        return self.start == None

    def printAll(self):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                print(temp.data, end = ' ')
                temp = temp.next

    def search(self, item):
        temp = self.start
        while temp is not None:
            if temp.data == item:
                print(f"found the item {item}")
                break
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

    def insert_after(self, data, after):
        if self.start == None:
            return -1
        newNode = Node(data = data)
        temp = self.start
        while temp is not None:
            if temp.data == after and temp.next == None:
                temp.next = newNode
                newNode.prev = temp
            elif temp.data == after:
                temp.next.prev = newNode
                newNode.next = temp.next
                temp.next = newNode
                newNode.prev = temp
            temp = temp.next

    def delete_first(self):
        if self.start == None:
            return -1
        if not self.is_empty():
            if self.start.next is None:
                self.start = None
            temp = self.start.next
            temp.prev = None
            self.start = temp

    def delete_last(self):
        if self.start == None:
            return -1
        if self.start.next is None:
            self.start = None
        temp = self.start
        while temp is not None:
            if temp.next.next == None:
                temp.next.prev = None        
                temp.next = None
            temp = temp.next

    def delete_after(self, after):
        if self.start == None:
            return -1
        if self.start.data == after:
            self.delete_first()
        temp = self.start.next
        while temp is not None:
            if temp.data == after:
                temp.prev.next = temp.next
                temp.next = None
                break
            elif temp.data == after and temp.next == None:
                self.delete_last()
            temp = temp.next


class DLLIterator:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        tempData = self.current.data
        self.current = self.current.next
        return tempData

#driver code

myList = DLL()

print(myList.is_empty())
print(myList.insert_first(4))
print(myList.insert_first(3))
print(myList.insert_first(2))
print(myList.insert_first(1))
print(myList.insert_last(5))
print(myList.insert_after(6, 5))
print(myList.insert_after(5.5, 5))
print(myList.search(4))
print(myList.printAll())
# print(myList.delete_first())
# print(myList.delete_last())
print(myList.delete_after(1))
for x in myList:
    print(x, end=' ')

