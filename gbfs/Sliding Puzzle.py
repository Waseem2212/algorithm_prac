from collections import deque

def slidingPuzzle(board):
    # Convert the board to a single string to represent the initial state
    start = ''.join(str(num) for row in board for num in row)
    target = "123450"
    
    # If the initial state is already the target
    if start == target:
        return 0

    # Define neighbors for each index in the 2x3 grid
    neighbors = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4],
        4: [1, 3, 5],
        5: [2, 4]
    }

    # BFS initialization
    queue = deque([(start, start.index('0'), 0)])  # (current_state, index_of_0, move_count)
    visited = {start}

    while queue:
        state, zero_idx, moves = queue.popleft()
        
        # Try moving the '0' to each neighboring position
        for neighbor in neighbors[zero_idx]:
            # Swap the '0' with the neighboring tile
            new_state = list(state)
            new_state[zero_idx], new_state[neighbor] = new_state[neighbor], new_state[zero_idx]
            new_state_str = ''.join(new_state)
            
            # If we've reached the target, return the move count
            if new_state_str == target:
                return moves + 1
            
            # If not visited, add to queue and mark as visited
            if new_state_str not in visited:
                visited.add(new_state_str)
                queue.append((new_state_str, neighbor, moves + 1))

    return -1  # If no solution is found
