def solveNQueens(n: int):
    board = []
    res = []
    for _ in range(n):
        board.append(["."]*n)
    def isSafe(row,col):
        row2 = row
        col2 = col
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -=1
            col -= 1
        row = row2
        col = col2
        while col >= 0:
            if board[row][col] == "Q":
                return False
            col -= 1
        row = row2
        col = col2
        while row < n and col >= 0:
            if board[row][col] == "Q":
                return False
            row += 1
            col -= 1
        return True
    
    def dfs(col):
        if col == n:
            sol = []
            for row in board:
                sol.append("".join(row))
            res.append(sol)
            return
        for i in range(n):
            if isSafe(i,col) == True:
                board[i][col] = "Q"
                print("col:",col)
                print("board:",board)
                dfs(col+1)
                board[i][col] = "."
    dfs(0)
    return res
print(solveNQueens(4))