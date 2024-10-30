def exist(board, word):
    rows, cols = len(board), len(board[0])

    # DFS function for the word search
    def dfs(r, c, index):
        if index == len(word):
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]:
            return False

        temp, board[r][c] = board[r][c], '#'  # Mark as visited
        found = (dfs(r + 1, c, index + 1) or
                 dfs(r - 1, c, index + 1) or
                 dfs(r, c + 1, index + 1) or
                 dfs(r, c - 1, index + 1))
        board[r][c] = temp  # Reset cell
        return found

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0] and dfs(r, c, 0):
                return True

    return False

# Example Execution
board_example = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]
word_example = "ABCCED"
print("Word Search Result:", exist(board_example, word_example))
