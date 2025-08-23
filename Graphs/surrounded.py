def solve(board):
    def checkBorders(stRow, stCol):
        nonlocal n, m
        zeroes = []
        for i in range(stRow, n):
            if board[i][stCol] == "O":
                zeroes.append((i, stCol))
                vis[i][stCol] = True
        for i in range(stCol + 1, m):
            if board[n - 1][i] == "O":
                zeroes.append((n - 1, i))
                vis[n - 1][i] = True

        for i in range(n - 2, -1, -1):
            if board[i][m - 1] == "O":
                zeroes.append((i, m - 1))
                vis[i][m - 1] = True

        for i in range(m - 2, 0, -1):
            if board[0][i] == "O":
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
                and board[r][c] == "O"
            ):
                vis[r][c] = True
                dfs((r, c))

    n = len(board)
    m = len(board[0])
    vis = []
    all = []
    for i in range(n):
        tmp = []
        for j in range(m):
            if board[i][j] == "O":
                all.append((i, j))
            tmp.append(False)
        vis.append(tmp)
    # print(vis)
    zeroes = checkBorders(0, 0)
    for i in zeroes:
        dfs(i)
    print(vis)
    for node in all:
        row = node[0]
        col = node[1]
        if not vis[row][col]:
            board[row][col] = "X"
    return board


print(
    solve(
        [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
    )
)
