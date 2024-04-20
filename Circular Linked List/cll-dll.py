class Node:
    def __init__(self, item=None, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next

class CLL:
    def __init__(self, start=None):
        self.start = start

    def isEmpty(self):
        return self.start is None

    def insert_At_first(self, data):
        node = Node(data)
        if not self.isEmpty():
            first_node = self.start
            node.next = first_node
            node.prev = self.start.prev
            first_node.prev = node
        else:
            node.prev = node
            node.next = node
        self.start = node
        return node

    def insert_At_last(self, data):
        node = Node(data)
        if not self.isEmpty():
            last_node = self.start.prev
            last_node.next = node
            self.start.prev = node
            node.prev = last_node
            node.next = self.start
        else:
            self.start = node
            node.prev = node
            node.next = node
        return node

    def search(self, data):
        temp = self.start
        while True:
            if temp.item == data:
                return f"item: {temp.item} found at {temp}"
            temp = temp.next
            if temp == self.start:
                break
        return f"item: {data} not found"

new = CLL()
print(new.isEmpty())
print(new.insert_At_first(1).item)
print(new.insert_At_first(2).item)
print(new.insert_At_first(3).item)
print(new.insert_At_first(4).item)
print(new.insert_At_last(5).item)
print(new.search(1))
