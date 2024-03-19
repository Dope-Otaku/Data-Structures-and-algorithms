# # singly linked list
# '''
#    created this node class where it has two items one is item(data) and another is next which points to next item 
# '''
# class Node:
#     def __init__(self, item=None, next=None):
#         self.item = item
#         self.next = next

# class Singly_list:
#     '''
#     created an empty sll with a head where there is no data but only address pointer is saved as self.start
#     '''
#     def __init__(self, start=None):
#         self.start = start
#     '''
#     created a method to check that if the list is empty or not
#     '''
#     def is_empty(self):
#         return self.start==None
#     '''
#     created an insert at start where we need to add a node between the head and and a node 
#     '''
#     def insert_at_start(self, data):
#         n = Node(data, self.start)
#         self.start = n
    
#     def insert_at_last(self, data):
#         n = Node(data)
#         if not self.is_empty():
#             temp = self.start
#             while temp.next is not None:
#                 temp = temp.next
#             temp.next = n 
#         else:
#             self.start = n



#     def search(self, data):
#         if not self.is_empty():
#             temp = self.start
#             while temp is not None:
#                 if temp.item == data:
#                     return f"Item found at {temp.item} and you searched for {data}"
#                 else:
#                     temp = temp.next
#         else:
#             return f"list is empty"


# # driver code
# mylist = Singly_list()

# print(mylist.is_empty())
# print(mylist.insert_at_start(10))
# print(mylist.search(1))




class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class Sll:
    def __init__(self, start=None):
        self.start = start

    def isEmpty(self):
        if self.start == None:
            return f"The singly linked list is empty"
        else:
            return f"the sll is not empty"
        
    
        
    def insert_at_first(self, data):
        try: 
            node = Node(data, self.start)
            self.start = node  # Update the start of the list to the new node
            print("node added at first")
        except:
            return f"failed to add a node at first"
        
    def insert_at_last(self, data):
        node = Node(data)
        if not self.isEmpty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = node
        else:
            self.start = node 

    def search(self, value):
        if not self.isEmpty():
            temp = self.start
            while temp is not None:
                if temp.item == value:
                    f"found at {temp}"
                else:
                    temp = temp.next
        else:
            return f"list is empty"

    def insertBefore(self, newdata, olddata):
        if not self.isEmpty():
            temp = self.start
            prev = None
            NewNode = Node(newdata)
            while temp is not None:
                if temp.item == olddata:
                    if prev is None:
                        NewNode.next = temp
                        self.start = NewNode
                    else:
                        prev.next = NewNode
                        NewNode.next = temp
                    return f"Inserted {newdata} before {olddata}"
                prev = temp
                temp = temp.next
            return f"Item {olddata} not found in the list"
        else:
            return f"List is empty"

        

        
    

ll =  Sll()
print(ll.insert_at_first(2))
print(ll.isEmpty())
print(ll.insert_at_last(7))
print(ll.search(2))
print(ll.insertBefore(9, 2))