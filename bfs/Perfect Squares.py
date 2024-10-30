from collections import deque

def numSquares(n):
    queue = deque([(n, 0)])
    visited = set()
    
    while queue:
        remaining, steps = queue.popleft()
        for i in range(1, int(remaining**0.5) + 1):
            new_remaining = remaining - i * i
            if new_remaining == 0:
                return steps + 1
            if new_remaining not in visited:
                visited.add(new_remaining)
                queue.append((new_remaining, steps + 1))
    
    return n
