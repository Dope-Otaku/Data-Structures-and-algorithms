'''
in this section we will learn about bfs in deep

1. in bfs we go level by level
2. we will use queue in this

'''

graph = {}


visited = [] #List for visited Nodes.
queue = [] #intialized a queue

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue: #creating a loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")