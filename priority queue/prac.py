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

    def pop(self):
        if self.item == []:
            raise EOFError("PQ has No elements")
        return self.item.pop(0)[0]

    def is_Empty(self):
        return len(self.item) == 0


    def size(self):
        return len(self.item)




# driver code

myList = PQ()

print(myList.push(2, 10))
print(myList.push(1, 9))
print(myList.push(3, 11))
print(myList.pop())
print(myList.size())
