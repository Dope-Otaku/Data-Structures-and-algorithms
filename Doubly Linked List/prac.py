#doubly linked list

class Node:
    def __init__(self, prev=None, next=None, item=None):
        self.prev = prev
        self.next = next
        self.item = item

class dll:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        if self.start is None:
            return f"List is empty"
        else:
            return f"List is not Empty!"
        
    def insertAtFirst(self, data):
        node = Node(None, self.start, data)

        if not self.is_empty():
            self.start.prev = node
            print(f"the list was not empty and hence added")
        self.start = node
        print(f"list was empty and hence added the node {node}")           
    
    def insertAtLast(self, data):
        node = Node(item = data)
        if self.start == None:
            self.start = node
            print(f"no earlier list found, ading at {self.start}")
            return 
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        temp.next = node
        node.prev = temp
        print(f"added at last using traversal")              

    def search(self, data):
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    print(f"found at: {temp.item} and you searched for {data}")
                    return  temp
                temp = temp.next
            return None
        
    def insertAfter(self, temp, data):
        if temp is not None:
            n = Node(temp, temp.next, data)
            if temp.next is not None:
                temp.next.prev = n
                # n.prev = temp as already assigned!
            temp.next = n

    def printl(self):
        temp = self.start
        while temp is not None:
            print(f"{temp.item}", end=" ")
            temp = temp.next


n = dll()
print(n)
print(n.insertAtFirst(1))
print(n.is_empty())
print(n.insertAtFirst(2))
print(n.insertAtLast(3))
print(n.is_empty())
print(n.search(3))
# print(n.insertAfter(3,4))
print(n.printl())