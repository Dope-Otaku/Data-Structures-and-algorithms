#implementing stack using inheriting list class
from prac import *    #in sll there are some issue with the code id what is happening

class Stack(Sll):

    def __init__(self):
        self.item_count = 0

    def is_empty(self):
        return super().isEmpty()   #by using super() we can call function of SLL or any other inherited class
     
    def push(self, data):
        # self.item_count +=1
        return super().insert_at_first(data)

    def pop(self):   #there is some bug with this method if you find any commit it so that everyone can benefit from it
        # if not self.is_empty():
            # self.item_count -=1
            val = self.start.item
            self.Delete(val)
            return f"deleted {val}"
    
    def peek(self):
         if not self.isEmpty():
              return self.start.item
         else:
              raise IndexError("Empty stack")

    def size(self):
         return f"{self.item_count}"




ll = Stack()

print(ll.push(1))
print(ll.push(2))
# print(ll.push(3))
# print(ll.pop()) #this works but deletes the last node only
print(ll.is_empty())
print(ll.peek())
print(ll.size())