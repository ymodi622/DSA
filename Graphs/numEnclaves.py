def numEnclaves(grid):
    def checkBorders(stRow, stCol):
        nonlocal n, m
        zeroes = []
        for i in range(stRow, n):
            if grid[i][stCol] == 1:
                zeroes.append((i, stCol))
                vis[i][stCol] = True
        for i in range(stCol + 1, m):
            if grid[n - 1][i] == 1:
                zeroes.append((n - 1, i))
                vis[n - 1][i] = True

        for i in range(n - 2, -1, -1):
            if grid[i][m - 1] == 1:
                zeroes.append((i, m - 1))
                vis[i][m - 1] = True

        for i in range(m - 2, 0, -1):
            if grid[0][i] == 1:
                zeroes.append((0, i))
                vis[0][i] = True

        return zeroes

    def dfs(node):
        row = node[0]
        col = node[1]
        if not vis[row][col]:
            vis[row][col] = True

        dRow = [-1, 0, 1, 0]
        dCol = [0, -1, 0, 1]

        for i in range(4):
            r = row + dRow[i]
            c = col + dCol[i]
            if (
                r >= 0
                and r < n
                and c >= 0
                and c < m
                and not vis[r][c]
                and grid[r][c] == 1
            ):
                vis[r][c] = True
                dfs((r, c))

    vis = []
    land = []
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        tmp = []
        for j in range(m):
            if grid[i][j] == 1:
                land.append((i, j))
            tmp.append(False)
        vis.append(tmp)
    ones = checkBorders(0, 0)
    for node in ones:
        dfs(node)
    res = 0
    for node in land:
        row = node[0]
        col = node[1]
        if not vis[row][col]:
            res += 1
    return res
