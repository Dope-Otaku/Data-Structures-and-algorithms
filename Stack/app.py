#stack using list

class SLL():
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
        if self.is_empty():
            return f"list is empty"
        for i in range(len(self.list)):
            if self.list[i] == data:
                self.list.remove(data)
                return f"deleted data: {data} from the stack"
            return f"not in the stack {data}"



new = SLL()
print(new.is_empty())
print(new.push(1))
print(new.pop(1))
print(new.is_empty())