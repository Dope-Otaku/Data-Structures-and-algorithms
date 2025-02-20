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

    def insertLast(self, item):
        newNode = Node(item)
        if not self.isEmpty():
            head = self.start
            while head.next != None:
                head  = head.next
            head.next = newNode
            return f"added  {item}"
        else:
            self.start = newNode
        
    def search(self, item):
        if not self.isEmpty():
            temp = self.start
            while temp.next is not None:
                if temp.data == item:
                    return f"data:{item} found at {temp}"
                temp =temp.next
            if temp.data == item:
                return f"data:{item} found at {temp}"
            else:
                return f"Data:{item} not available in list"
        else:
            return f"list is empty"


    def traverse(self):
        temp = self.start
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next

    def insertAfter(self, item, data):
        temp = self.start
        newNode = Node(data)
        while temp is not None:
            print(temp.data)
            if temp.data == item:
                newNode.next = temp.next
                temp.next = newNode #problem solved
                return f"inserted after {item}"
            temp = temp.next

    def deleteFirst(self):
        if not self.isEmpty():
            self.start = self.start.next

    def deleteLast(self):
        if self.start == None:
            return -1

        elif self.start.next == None:
            self.start = None
        if not self.isEmpty():
            temp = self.start
            while temp.next.next is not None:
                    temp = temp.next
            temp.next = None
                
    def deleteItem(self, item):
        if self.start == None:
            return -1

        elif self.start.next == None and self.start.data == data:
            self.start = None
        
        else:
            temp = self.start
            if temp.data == item:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.data == item:
                        temp.next = temp.next.next
                        break
                    temp = temp.next


    def __iter__(self):
        return SLLIterator(self.start)

    def reverseList(self):
        listo = []
        temp = self.start
        while temp is not None:
            listo.append(temp.data)
            temp = temp.next
        for i in reversed(listo):
            print(i)
        # return revList

class SLLIterator():
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        dataTemp = self.current.data
        self.current = self.current.next
        return dataTemp



#drivers code
myList = SLL()

print(myList.isEmpty())
print(myList.insertFront(1))
print(myList.insertFront(2))
print(myList.currentPointer())
print(myList.insertLast(3))
print(myList.insertAfter(3,4))
print(myList.search(4))
print(myList.traverse())
# print(myList.deleteFirst())
# print(myList.deleteLast())
print(myList.deleteItem(3))
print(myList.traverse())
# print(myList.reverseList())

# for x in myList:
#     print(x, end=' ')

