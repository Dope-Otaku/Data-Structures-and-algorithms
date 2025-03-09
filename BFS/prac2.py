# graph = {
#     '9': ['7'],
#     '7': [ '5'],
#     '5': ['4'],
#     '4': ['3', '2'],
#     '3': [],
#     '2': []
# }
graph = {
      '0': ['1', '3', '2'],
      '1': [],
      '3': [],
      '2': ['4'],
      '4': []
}


visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)



bfs(visited, graph, '0')
# bfs(visited, graph, '5')