'''

priority queue
'''




class PQ:
    def __init__(self):
        self.item = []

    def push(self, data, priority):
        index = 0
        while index<len(self.item) and self.item[index][1]<=priority:
            index+=1
        self.item.insert(index, (data, priority))





# driver code

myList = PQ()

