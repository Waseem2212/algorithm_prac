def numIslands(grid):
    # If the grid is empty, return 0 as there are no islands
    if not grid:
        return 0

    # DFS function to mark all cells in an island as visited
    def dfs(i, j):
        # Check boundaries and if the cell is water ('0')
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
            return
        grid[i][j] = '0'  # Mark cell as visited by setting it to '0'
        
        # Visit all neighboring cells in four directions
        dfs(i+1, j)  # Down
        dfs(i-1, j)  # Up
        dfs(i, j+1)  # Right
        dfs(i, j-1)  # Left

    count = 0  # Counter for the number of islands
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If cell is land ('1'), we found a new island
            if grid[i][j] == '1':
                dfs(i, j)  # Mark the island cells
                count += 1  # Increment island count
    return count


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
