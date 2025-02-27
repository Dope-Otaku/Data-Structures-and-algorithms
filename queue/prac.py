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




# driver code
myList = Queue()