def exist(board, word: str) -> bool:
    rowCnt = len(board)
    colCnt = len(board[0])
    n = len(word)
    
    def dfs(sub, ind, row, col, visited):
        if sub != word[:ind+1]:
            return False
        if sub == word:
            return True
        
        visited.add((row, col))
        found = False
        
        # Move right
        if col < colCnt - 1 and (row, col + 1) not in visited:
            nextSub = sub + board[row][col + 1]
            found = dfs(nextSub, ind + 1, row, col + 1, visited)
        # Move left
        if not found and col > 0 and (row, col - 1) not in visited:
            nextSub = sub + board[row][col - 1]
            found = dfs(nextSub, ind + 1, row, col - 1, visited)
        # Move down
        if not found and row < rowCnt - 1 and (row + 1, col) not in visited:
            nextSub = sub + board[row + 1][col]
            found = dfs(nextSub, ind + 1, row + 1, col, visited)
        # Move up
        if not found and row > 0 and (row - 1, col) not in visited:
            nextSub = sub + board[row - 1][col]
            found = dfs(nextSub, ind + 1, row - 1, col, visited)
        
        visited.remove((row, col))
        return found

    for i in range(rowCnt):
        for j in range(colCnt):
            if board[i][j] == word[0]:
                if dfs(board[i][j], 0, i, j, set()):
                    return True
    return False

# Test
print(exist(
    [["A","B","C","E"],
     ["S","F","C","S"],
     ["A","D","E","E"]],
    "ABCCED"
))

#optimzed

def exist(board, word: str) -> bool:
    rowCnt = len(board)
    colCnt = len(board[0])
    
    def dfs(row, col, ind, visited):
        if ind == len(word):
            return True
        if (row < 0 or row >= rowCnt or
            col < 0 or col >= colCnt or
            (row, col) in visited or
            board[row][col] != word[ind]):
            return False
        
        visited.add((row, col))
        # Try all 4 directions
        found = (dfs(row+1, col, ind+1, visited) or
                 dfs(row-1, col, ind+1, visited) or
                 dfs(row, col+1, ind+1, visited) or
                 dfs(row, col-1, ind+1, visited))
        visited.remove((row, col))
        return found
    
    for r in range(rowCnt):
        for c in range(colCnt):
            if board[r][c] == word[0] and dfs(r, c, 0, set()):
                return True
    return False

# Test case
print(exist(
    [["A","B","C","E"],
     ["S","F","C","S"],
     ["A","D","E","E"]],
    "ABCCED"
))  # Output: True
