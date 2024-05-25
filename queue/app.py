# queue data structure implementation using list


class Queue:
    def __init__(self):
        self.item = []
        self.front = None
        self.rear = None

    def enqueue(self, data):
        self.item.append(data)
        return "added succcessfully"

    def itemQ(self):
        print(self.item)

    def is_empty(self):
        if self.item == None:
            return "Queue is empty"
        return "Queue is not empty"
        
    def get_front(self):
        return self.item[0]
    
    def get_rear(self):
        return self.item[len(self.item)-1]

    def dequeue(self):
        self.item.pop(0)
        return "deleted succcessfully"

l = Queue()

print(l.enqueue(1))
print(l.enqueue(2))
print(l.enqueue(3))
print(l.dequeue(3))
print(l.itemQ())
print(l.get_front())
print(l.get_rear())