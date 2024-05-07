#implementing stack using inheriting list class
from prac import *    #in sll there are some issue with the code id what is happening

class Stack(Sll):
    def is_empty(self):
        return super().isEmpty()   #by using super() we can call function of SLL or any other inherited class
     
    def push(self, data):
        return super().insert_at_first(data)

    def pop(self):   #there is some bug with this method if you find any commit it so that everyone can benefit from it
        # if not self.is_empty():
            val = self.start.item
            self.Delete(val)
            return f"deleted {val}"
    
ll = Stack()

print(ll.push(1))
print(ll.push(2))
# print(ll.push(3))
print(ll.pop()) #this works but deletes the last node only
print(ll.is_empty())