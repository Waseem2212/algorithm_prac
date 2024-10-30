import heapq

def minimumEffortPath(heights):
    rows, cols = len(heights), len(heights[0])
    effort_grid = [[float('inf')] * cols for _ in range(rows)]
    effort_grid[0][0] = 0
    min_heap = [(0, 0, 0)]  # (effort, row, col)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while min_heap:
        current_effort, x, y = heapq.heappop(min_heap)
        
        # If we reach the bottom-right cell
        if (x, y) == (rows - 1, cols - 1):
            return current_effort

        # Explore all four directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                next_effort = max(current_effort, abs(heights[nx][ny] - heights[x][y]))
                
                # Update the cell if the next effort is smaller
                if next_effort < effort_grid[nx][ny]:
                    effort_grid[nx][ny] = next_effort
                    heapq.heappush(min_heap, (next_effort, nx, ny))

    return 0
