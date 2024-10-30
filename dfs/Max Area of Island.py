def maxAreaOfIsland(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    max_area = 0

    # DFS function to calculate area of the island
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
            return 0
        grid[r][c] = 0  # Mark cell as visited
        area = 1  # Initial area of this cell
        # Explore all 4 directions
        area += dfs(r + 1, c)
        area += dfs(r - 1, c)
        area += dfs(r, c + 1)
        area += dfs(r, c - 1)
        return area

    # Main loop to find the max area of islands
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                max_area = max(max_area, dfs(r, c))

    return max_area

# Example Execution
grid_example = [
    [0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 1, 0, 1, 1]
]

print("Max Area of Island:", maxAreaOfIsland(grid_example))
