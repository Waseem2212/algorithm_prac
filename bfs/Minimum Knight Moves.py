from collections import deque

def minKnightMoves(x, y):
    directions = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]
    queue = deque([(0, 0, 0)])  # (current_x, current_y, moves)
    visited = set((0, 0))
    
    x, y = abs(x), abs(y)  # Symmetry in chessboard
    
    while queue:
        cx, cy, moves = queue.popleft()
        if (cx, cy) == (x, y):
            return moves
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if (nx, ny) not in visited and nx >= -2 and ny >= -2:
                visited.add((nx, ny))
                queue.append((nx, ny, moves + 1))
    
    return -1
