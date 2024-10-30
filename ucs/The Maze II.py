import heapq

def shortestDistance(maze, start, destination):
    rows, cols = len(maze), len(maze[0])
    distances = [[float('inf')] * cols for _ in range(rows)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    distances[start[0]][start[1]] = 0
    min_heap = [(0, start[0], start[1])]  # (distance, x, y)

    while min_heap:
        current_distance, x, y = heapq.heappop(min_heap)
        
        if [x, y] == destination:
            return current_distance
        
        # Explore all directions
        for dx, dy in directions:
            nx, ny, steps = x, y, 0
            
            # Roll the ball until it hits a wall
            while 0 <= nx + dx < rows and 0 <= ny + dy < cols and maze[nx + dx][ny + dy] == 0:
                nx += dx
                ny += dy
                steps += 1
            
            new_distance = current_distance + steps
            
            # If found a shorter path, update and push to heap
            if new_distance < distances[nx][ny]:
                distances[nx][ny] = new_distance
                heapq.heappush(min_heap, (new_distance, nx, ny))

    return -1  # Destination is unreachable
