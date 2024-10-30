def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
        visited.add(start)

    print(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

if __name__ == "__main__":
    dfs(graph, 'A')