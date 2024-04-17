#circular linked list

class Node:
    def __init__(self, item=None , next=None):
        self.item = item
        self.next = next
class CLL:
    def __init__(self, start=None):
        self.start = start

    def isEmpty(self):
        if self.start == None:
            return True
        return False

    def insertatFirst(self, data):
        if self.isEmpty():
            node = Node(data, self.start)
            self.start = node
            return f"added succesfully"
        return f"failed to add"


new = CLL()

print(new)
print(new.insertatFirst(9))
print(new.isEmpty())