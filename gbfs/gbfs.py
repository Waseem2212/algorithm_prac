import heapq

def heuristic(node, goal):
    # Example heuristic function; adjust as needed
    return abs(goal - node)

def greedy_best_first_search(graph, start, goal):
    priority_queue = [(heuristic(start, goal), start)]  # (heuristic, node)
    visited = set()

    while priority_queue:
        _, node = heapq.heappop(priority_queue)
        
        if node in visited:
            continue
        visited.add(node)
        
        if node == goal:
            return True

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic(neighbor, goal), neighbor))
    
    return False  # if no path found
