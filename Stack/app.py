#stack using list
# stack using inherited lst and 

class Stack():
    def __init__(self, item = None):
        self.list = []
        self.item = item
        
    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, item):
        if self.is_empty():
            self.list.append(item)
            return f"added | list was empty"
        self.list.append(item)
        return f"added | list was not empty"
    
    def pop(self, data):
        if not self.is_empty():
            self.list.remove(data)
            return f"stack is deleted"
        else:
            raise IndexError("stack is empty!")


    def peek(self):
        if not self.is_empty():
            val = self.list[-1]
            return val
        else:
            raise IndexError("stack is empty!")


    def size(self):
        if not self.is_empty():
            return f"the size of stack is {len(self.list)}"
        else:
            raise IndexError("stack is empty")

new = Stack()
print(new.is_empty())
print(new.push(1))
print(new.push(2))
# print(new.pop(1))
print(new.peek())
print(new.size())
print(new.is_empty())