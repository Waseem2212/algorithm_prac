def longestIncreasingPath(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    memo = [[-1] * cols for _ in range(rows)]

    def dfs(r, c):
        if memo[r][c] != -1:
            return memo[r][c]

        max_path = 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                max_path = max(max_path, 1 + dfs(nr, nc))

        memo[r][c] = max_path
        return max_path

    result = 0
    for r in range(rows):
        for c in range(cols):
            result = max(result, dfs(r, c))

    return result

# Example Execution
matrix_example = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]
print("Longest Increasing Path Result:", longestIncreasingPath(matrix_example))
