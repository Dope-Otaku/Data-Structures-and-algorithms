#we will be implementing a priority queue using list and also we have to take one points to consider that we have to sort based on priority let's start!

class Pq:
    def __init__(self):
        self.item = []

    def push(self, data, role):
        index = 0
        while index<len(self.item) and self.item[index][1]<=role:
            index += 1
            print("searching...")
        print(f"inserting at {index}")
        self.item.insert(index, (data, role))
        return f"added successfully"

    #this function is only for testing and not included in priority queue functions! i might have done it earlier so just ignore those...
    def printal(self):
        return self.item
    
    def is_Empty(self):
        if self.item == []:
            return f"empty hai"
        return False

    def pop(self):
        if not self.is_Empty():
            return self.item.pop(0)[0]  #can be return self.item.pop(0)
    
    def size(self):
        return len(self.item)

q = Pq()

print(q.push(10,6))
print(q.push(20,4))
print(q.push(30,2))
print(q.push(40,1))
print(q.push(50,3))
print(q.push(60,5))
print(q.size())
print(q.pop())
print(q.printal())
print(q.size())