class Queue:
    def __init__(self):
        self.item = []

    def is_Empty(self):
        if self.item == []:
            return True
        return False 
    
    def view(self):
        return f"{self.item}" 
    
    def enqueue(self, data):
        self.item.append(data)
        return f"successfully added {data} "

    def dequeue(self):
        Dvalue = self.item[0]
        self.item.pop(0)
        return f"successfully deleted {Dvalue}"
    
    def get_front(self):
        return self.item[0]
    
    def get_rear(self):
        return self.item[len(self.item)-1]
    
    def size(self):
        return len(self.item)
    

a = Queue()
print(a.is_Empty())
print(a.enqueue(1))
print(a.enqueue(2))
print(a.enqueue(3))
print(a.view())
print(a.dequeue())
print(a.view())
print(a.get_front())
print(a.get_rear())
print(a.size())
print(a.is_Empty())

