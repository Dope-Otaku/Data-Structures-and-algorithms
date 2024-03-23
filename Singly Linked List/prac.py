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



# ----------------------------------------------Practise-----------------------------------------------------------------
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
        if  self.isEmpty():
            node = Node(data, self.start)
            self.start = node  # Update the start of the list to the new node
            print("node added at first")
        else:
            return 0
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
        if self.isEmpty() is not None:
            temp = self.start
            while temp is not None:
                if temp.item == value:
                    return f"found this {value} at {temp}"  # Return the found item
                else:
                    temp = temp.next
            return f"Item {value} not found in the list"  # Return a message if item is not found
        else:
            return f"list is empty"  # Return a message if the list is empty
    def InsertBefore(self, Ev, Nv):
        if  self.isEmpty() != None:
            temp = self.start
            node = Node(Nv)
            while temp is not None:
                if temp.item == Ev:
                    node.next = temp
                    if temp == self.start:
                        self.start = node
                    else:
                        prev.next = node
                    print("success")
                    return
                prev = temp
                temp = temp.next
            else:
                return f"failed"
        else:
            return f'list is empty'
    def Delete(self, value):
        if self.isEmpty() != None:
            temp = self.start
            prev = None
            while temp is not None:
                if temp.item == value:
                    if prev is not None:
                        prev.next = temp.next
                    else:
                        self.start = temp.next
                    temp.next = None
                    return f"Node deleted with item {value}"
                prev = temp
                temp = temp.next
    def print_list(self):
        temp = self.start
        while temp != None:
            print(temp.item, end=' ')
            temp = temp.next

    def findMid(self):
        temp = self.start
        temp2 = self.start

        while temp2 is not None and temp2.next is not None:
            temp = temp.next
            temp2 = temp2.next.next
        return temp.item
    def sortList(self):
        return f"you can not sort a linked list"

    

ll =  Sll()
print(ll.insert_at_first(2))
# print(ll.isEmpty())
# print(ll.insert_at_last(7))  //error in this function fix it
print(ll.InsertBefore(2, 3))
print(ll.InsertBefore(3, 4))
print(ll.InsertBefore(4, 5))
print(ll.InsertBefore(5, 6))
print(ll.InsertBefore(6, 7))
print(ll.InsertBefore(7, 8))
print(ll.InsertBefore(8, 9))
# print(ll.search(2))
# print(ll.search(9))
# print(ll.search(1))
# print(ll.Delete(2))
# print(ll.search(2))
# print()
ll.print_list()
print("\n", ll.findMid())
print(ll.sortList())