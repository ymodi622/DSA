def ratInMaze(maze):
    
    
    n = len(maze)
    if maze[n-1][n-1] == 0:
        return []
    res = []
    visit = []
    for _ in range(n):
        visit.append([False]*n)
    def dfs(row,col,sol):
        print(row,col,sol)
        if row < 0 or col < 0 or row >= n or col >= n or maze[row][col] == 0 or visit[row][col]:
            return
        
        if row == n-1 and col == n-1:
            res.append(sol)
            return
        visit[row][col] = True
        if col != n-1:
            if maze[row][col+1] == 1:
                sol += "R"
                dfs(row,col+1,sol)
                sol = sol[:-1]
        if col != 0:
            if maze[row][col-1] == 1:
                sol += "L"
                dfs(row,col-1,sol)
                sol = sol[:-1]
        if row != n-1:
            if maze[row+1][col] == 1:
                sol += "D"
                dfs(row+1,col,sol)
                sol = sol[:-1]
        if row != 0:
            if maze[row-1][col] == 1:
                sol += "U"
                dfs(row-1,col,sol)
                sol = sol[:-1]
        visit[row][col] = False
        
    if maze[0][0] == 1:
        dfs(0,0,"")
    return res
print(ratInMaze([[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]])) 