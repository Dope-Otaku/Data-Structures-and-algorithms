#grpah is a special case of tree



class Graph:
    def __init__(self, vertex=None):
        self.vertex_count = vertex
        self.adj_matrix = [ [0]*vertex for _ in range(vertex) ]

    def add_edge(self, u, v, weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
        else:
            return f"invalid vertex"

    def remove_edge(self, u, v, weight=0):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
        else:
            return f"invalid vertex"


    def has_edge(self, u, v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return self.adj_matrix[u][v] != 0
        else:
            return f"Invalid Vertex"

    def print_adj_matrix(self):
        for row_list in self.adj_matrix:
            print(" ".join(map(str, row_list)))



#driver code

myList = Graph(5)

print(myList.add_edge(2,4))
print(myList.add_edge(1,4))
print(myList.add_edge(2,2))
print(myList.add_edge(0,4))
print(myList.add_edge(0,0))
print(myList.has_edge(0,0))
print(myList.print_adj_matrix())
print(myList.remove_edge(0,0))
print(myList.print_adj_matrix())