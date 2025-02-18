class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SLL():
    def __init__(self, start=None):
        self.start = start

    def isEmpty(self):
        return self.start==None

    def iterator(self):
        return SLLIterator(self.start)
    
    def printAll(self):
        temp = self.start
        while temp is not None:
            print(temp)
            temp = temp.next


class SLLIterator():
    def __init__(self):
        self.current = current

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        tempData = self.current.data
        self.current = self.current.next