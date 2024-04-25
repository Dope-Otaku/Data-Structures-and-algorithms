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
            return f"it is empty"
        if self.start == self.start.next:
            print(self.start.item) #the node value which is being deleted is this
            self.start = None
            return f'we deleted the only node'
        #first we exchange the last node pointer to second node
        last_node = self.start.prev
        first_node_item = self.start.item
        print(last_node.item)
        self.start.next.prev = last_node
        last_node.next = self.start.next
        #change the pointer to next
        self.start = self.start.next
        return f"deleted the first node ({first_node_item})"

    def delete_at_last(self):
        if self.isEmpty():
            return f"it is empty"
        if self.start == self.start.next:
            print(self.start.item) #the node value which is being deleted is this
            self.start = None
            return f'we deleted the only node'
        #last_node
        last_node = self.start.prev
        last = last_node.item
        new_node = last_node.prev
        self.start.prev = new_node
        new_node.next = self.start
        return f"deletetd the last element {last}"

    def delete_item(self, data):
        if self.start is not None:
            if self.start.next == self.start:
                if self.start.item == data:
                    self.start = None 
            else:
                temp = self.start
                if temp.item == data:
                    self.delete_at_first()
                else:
                    temp =temp.next
                    while temp.item is not self.start:
                        if temp.item == data:
                            temp.next.prev = temp.prev
                            temp.prev.next = temp.next
                            return f"deleted"
    #delet _item needs modification as the code is not working properly 

    def printlist(self):
        temp = self.start
        if temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
            while temp is not self.start:
                print(temp.item, end=" ")
                temp = temp.next

    def __iter__(self):
        return CDLLIterator(self.start)

class CDLLIterator:
    def __init__(self, start):
        self.current = start
        self.start = start

    def __iter__(self):
        return self

new = CLL()
print(new.isEmpty())
print(new.insert_At_first(1).item)
print(new.insert_At_first(2).item)
print(new.insert_At_first(3).item)
print(new.insert_At_last(5).item)
print(new.insert_after(3, 4))
# print(new.search(4))
# print(new.delete_after())

# print(new.delete_at_first())
# print(new.delete_item(1))
print(new.printlist())
print(new.isEmpty())

