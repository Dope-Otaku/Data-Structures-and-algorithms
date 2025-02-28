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