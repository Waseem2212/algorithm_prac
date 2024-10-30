import heapq

def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start)]  # (cost, node)
    visited = set()

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)
        
        if node in visited:
            continue
        visited.add(node)
        
        if node == goal:
            return cost

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor))
    
    return float("inf")  # if no path found
