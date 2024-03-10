# singly linked list
'''
   created this node class where it has two items one is item(data) and another is next which points to next item 
'''
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Singly_list:
    '''
    created an empty sll with a head where there is no data but only address pointer is saved as self.start
    '''
    def __init__(self, start=None):
        self.start = start
    '''
    created a method to check that if the list is empty or not
    '''
    def is_empty(self):
        return self.start==None
    '''
    created an insert at start where we need to add a node between the head and and a node 
    '''
    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n
    
    def insert_at_last(self, data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n 
        else:
            self.start = n

    def search(self, data):
        if not self.is_empty():
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    return f"Item found at {temp.item} and you searched for {data}"
                else:
                    temp = temp.next
        else:
            return f"list is empty"


# driver code
mylist = Singly_list()

print(mylist.is_empty())
print(mylist.search(1))