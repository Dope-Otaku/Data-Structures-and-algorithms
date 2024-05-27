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

    def printal(self):
        return self.item
    
q = Pq()

print(q.push(10,6))
print(q.push(20,4))
print(q.push(30,2))
print(q.push(40,1))
print(q.push(50,3))
print(q.push(60,5))
print(q.printal())