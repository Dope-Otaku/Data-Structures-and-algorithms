#stack using list

class SLL():
    def __init__(self, item = None):
        self.list = []
        self.item = item
        
    def is_empty(self):
        if self.list == []:
            return True

    def push(self, item):
        if self.is_empty():
            self.list.append(item)
            return f"added | list was empty"
        self.list.append(item)
        return f"added | list was not empty"



new = SLL()
print(new.is_empty())
print(new.push(1))
print(new.is_empty())