class Graph:
    def __init__(self, vno):
        self.vertex_count = vno
        self.adj_list = {v:[] for v in range(vno)}
#hello this is a remp function


    def add_edge(self, u, v, weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))
        else:
            return f"invalid vertex"
#hello this is a remp function
            

    def remove_edge(self, u, v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u] = [(vertex, weight) for vertex, weight in self.adj_list[u] if vertex!=v]
            self.adj_list[v] = [(vertex, weight) for vertex, weight in self.adj_list[v] if vertex!=u]
        else:
            return f"invalid vertex"

    def has_edge(self, u, v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return any(vertex == v for vertex, x in self.adj_list[u])

    def print_adj_list(self):
        v = 0
        for vertex, c in self.adj_list.items():
            print(f"V{v}-> {vertex}:{c}")
            v+=1


#driver code

myList = Graph(5)

print(myList.add_edge(2,4))
print(myList.add_edge(1,4))
print(myList.add_edge(2,2))
print(myList.add_edge(0,4))
print(myList.add_edge(0,0))
print(myList.has_edge(0,0))
print(myList.print_adj_list())
print(myList.remove_edge(0,0))
print(myList.print_adj_list())
