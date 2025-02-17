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


    # def traverse(self):
    #     temp = self.start
    #     while temp.next is not None:
    #         print(self.start.data)
    #         temp = temp.next






#drivers code
myList = SLL()

print(myList.isEmpty())
print(myList.insertFront(1))
print(myList.insertFront(2))
# print(myList.currentPointer())
print(myList.insertLast(3))
# print(myList.traverse())
print(myList.search(4))