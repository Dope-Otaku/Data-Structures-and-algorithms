#circular doubly linked list

class Node:
    def __init__(self, item=None, prev=None, next=None):
        self.item = item
        self.prev= prev
        self.next = next

class CLL:
    def __init__(self, start=None):
        self.start = start

    def isEmpty(self):
        return self.start==None

    def insert_At_first(self, data):
        node = Node(data)
        if not self.isEmpty():
            first_node = self.start
            node.next = first_node
            node.prev = self.start.prev
            return node
        else:
            node.prev = self.start
            node.next = node
            return node
    def insert_At_last(self, data):
        node = Node(data)
        if not self.isEmpty():
            last_node = self.start.prev
            last_node.next = node
            self.start.prev = node
            node.next = self.start
            return node
        self.start = node.prev
        node.next = node
        return node
        

new = CLL()
print(new.isEmpty())
print(new.insert_At_first(1).item)
print(new.insert_At_last(5).item)