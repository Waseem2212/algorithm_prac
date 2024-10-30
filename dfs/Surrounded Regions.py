def solve(board):
    if not board:
        return

    rows, cols = len(board), len(board[0])

    # DFS to mark 'O' connected to borders
    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
            return
        board[r][c] = '#'  # Temporarily mark the cell
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # Step 1: Start DFS from all 'O's on the border
    for r in range(rows):
        for c in range(cols):
            if (r in {0, rows - 1} or c in {0, cols - 1}) and board[r][c] == 'O':
                dfs(r, c)

    # Step 2: Convert all 'O' to 'X' (surrounded ones) and '#' back to 'O'
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == '#':
                board[r][c] = 'O'

# Example Execution
board_example = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]

solve(board_example)
print("Surrounded Regions Result:", board_example)
