'''
queue u8ses fifo method first in first out method!

insertion-> enqueue
deletion-> dequque
'''




class Queue:
    def __init__(self, front=None, rear=None):
        self.arr = []
        self.front = front
        self.rear = rear

    def get_front(self):
        return self.arr[0]

    def get_rear(self):
        return self.arr[-1]

    def is_empty(self):
        return self.arr == []

    def enqueue(self,data):
        return self.arr.append(data)

    def dequeue(self):
        pass




# driver code
myList = Queue()

print(myList.is_empty())
print(myList.enqueue(1))
print(myList.enqueue(2))
print(myList.get_front())
print(myList.get_rear())
