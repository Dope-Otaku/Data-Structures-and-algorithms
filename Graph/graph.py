class Graph:
    def __init__(self, vno):
        self.vertex_count = vno
        self.adj_list = {v:[] for v in range(vno)}


    def add_edge(self, u, v, weight=1):
        pass