def pacificAtlantic(heights):
    rows, cols = len(heights), len(heights[0])
    pacific_reachable = set()
    atlantic_reachable = set()
    
    def bfs(starts, reachable):
        queue = deque(starts)
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c] and (nr, nc) not in reachable:
                    reachable.add((nr, nc))
                    queue.append((nr, nc))

    pacific = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
    atlantic = [(rows-1, c) for c in range(cols)] + [(r, cols-1) for r in range(rows)]
    
    bfs(pacific, pacific_reachable)
    bfs(atlantic, atlantic_reachable)
    
    return list(pacific_reachable & atlantic_reachable)
