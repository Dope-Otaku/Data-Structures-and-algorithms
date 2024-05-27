#implementation of deque using list

class Deque:
    def __init__(self):
        self.item = []

    def insert_front(self, data):
        self.item.insert(0, data)
        return f"inserted at front successfully!"
    
    def insert_rear(self, data):
        self.item.append(data)
        return f"inserted at rear successfully!"

q = Deque()

print(q.insert_front(1))
print(q.insert_front(3))
print(q.insert_front(4))
print(q.insert_front(5))
print(q.insert_rear(2))