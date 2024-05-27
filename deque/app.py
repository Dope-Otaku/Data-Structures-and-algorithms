#implementation of deque using list

class Deque:
    def __init__(self):
        self.item = []

    def print_all(self):
        return self.item
    def is_empty(self):
        if self.item == []:
            return f"Deque is empty!"
        return f"Deque is not empty!"

    def insert_front(self, data):
        self.item.insert(0, data)
        return f"inserted at front successfully!"
    
    def insert_rear(self, data):
        self.item.append(data)
        return f"inserted at rear successfully!"
    
    def get_rear(self):
        return self.item[len(self.item)-1]
    def get_front(self):
        return self.item[0]
    
    def delete_front(self):
        print(f"deleted the the first element {self.get_front()}")
        self.item.remove(self.get_front())
    
    def delete_rear(self):
        print(f"deleted the the first element {self.get_rear()}")
        self.item.pop()

    def size(self):
        return len(self.item)

q = Deque()


print(q.is_empty())
print(q.insert_front(1))
print(q.insert_front(3))
print(q.insert_front(4))
print(q.insert_front(5))
print(q.insert_rear(2))
print(q.get_rear())
print(q.get_front())
print(q.print_all())
print(q.delete_front())
print(q.print_all())
print(q.delete_rear())
print(q.print_all())
print(q.is_empty())
print(q.size())