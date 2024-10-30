def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    island_count = 0

    # DFS function to mark the connected '1's
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        grid[r][c] = '0'  # Mark the cell as visited
        # Visit all 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # Main loop to visit each cell
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':  # Found an unvisited island part
                dfs(r, c)
                island_count += 1

    return island_count

# Example Execution
grid_example = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print("Number of Islands:", numIslands(grid_example))
