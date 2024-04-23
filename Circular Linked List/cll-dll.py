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
        if temp is None:
            return None
        if temp.item==data:
            return f"{temp.item} found at temp"
        while True:
            if temp.item == data:
                return f"item: {temp.item} found at {temp}"
            temp = temp.next
            if temp == self.start:
                break
        return f"item: {data} not found"

    def insert_after(self, after_item, data):
        if self.isEmpty():
            print("List is empty.")
            return
        
        # Search for the node with the given item value
        temp = self.start
        while True:
            if temp.item == after_item:
                break
            temp = temp.next
            if temp == self.start:
                print(f"Item {after_item} not found.")
                return

        node = Node(data)

        # If the found node is the last node
        if temp == self.start.prev:
            self.insert_At_last(data)
            return

        # Update the next pointers
        node.next = temp.next
        temp.next.prev = node

        # Update the prev pointers
        temp.next = node
        node.prev = temp

        return(f"Inserted {data} after {after_item}.")

    def delete_at_first(self):
        if self.isEmpty():
            return f"it is emoty"
        if self.start == self.start.next:
            print(self.start.item) #the node value which is being deleted is this
            self.start = None
            return f'we deleted the only node'
        
        



new = CLL()
# print(new.isEmpty())
# print(new.insert_At_first(1).item)
# print(new.insert_At_first(2).item)
# print(new.insert_At_first(3).item)
print(new.insert_At_last(5).item)
# print(new.insert_after(3, 4))
# print(new.search(4))
print(new.isEmpty())

print(new.delete_at_first())
print(new.isEmpty())

