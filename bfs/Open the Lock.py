from collections import deque

def openLock(deadends, target):
    dead_set = set(deadends)
    if '0000' in dead_set:
        return -1
    
    queue = deque([('0000', 0)])
    visited = set('0000')

    while queue:
        code, steps = queue.popleft()
        if code == target:
            return steps
        for i in range(4):
            for d in [-1, 1]:  # Rotate digits up and down
                new_digit = (int(code[i]) + d) % 10
                new_code = code[:i] + str(new_digit) + code[i+1:]
                if new_code not in dead_set and new_code not in visited:
                    visited.add(new_code)
                    queue.append((new_code, steps + 1))
    
    return -1
