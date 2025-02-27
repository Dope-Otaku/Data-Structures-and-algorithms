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

    def enqueue(self,data):
        return self.arr.append(data)




# driver code
myList = Queue()

print(myList.enqueue(1))