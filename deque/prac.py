'''
dequeu is basically double ended queue with no restriction

'''

class Deque:
    def __init__(self):
        self.arr = []

    def insert_front(self, item):
        return self.arr.insert(0, item)

    def insert_rear(self, item):
        return self.arr.append(item)

    def size(self):
        return len(self.arr)

    def is_empty(self):
        return self.arr == []


    def delete_front(self):
        return self.arr.pop(0)

#driver code

myList = Deque()

print(myList.insert_front(4))
print(myList.insert_front(3))
print(myList.insert_front(2))
print(myList.insert_front(1))
print(myList.size())