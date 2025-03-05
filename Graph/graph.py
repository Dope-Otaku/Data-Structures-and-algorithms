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
        pass