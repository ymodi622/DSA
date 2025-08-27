def countDistinctIslands(grid):
    n = len(grid)
    m = len(grid[0])
    vis = [[False for j in range(m)] for i in range(n)]

    # print(vis)
    dRow = [-1, 0, 1, 0]
    dCol = [0, -1, 0, 1]
    shapes = set()

    def dfs(row, col, base_row, base_col, arr):
        vis[row][col] = True
        arr.append((row - base_row, col - base_col))
        for i in range(4):
            r = row + dRow[i]
            c = col + dCol[i]
            if 0 <= r < n and 0 <= c < m and not vis[r][c] and grid[r][c] == 1:
                dfs(r, c, base_row, base_col, arr)

    for r in range(n):
        for c in range(m):
            if grid[r][c] == 1 and not vis[r][c]:
                arr = []
                dfs(r, c, r, c, arr)
                shapes.add(tuple(arr))
    return len(shapes)


print(
    countDistinctIslands(
        [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
    )
)
print(
    countDistinctIslands(
        [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    )
)
