from collections import deque, defaultdict


def orangesRotting(grid):

    n1 = len(grid)
    n2 = len(grid[0])
    cnt = 0
    q = deque()
    vis = []
    time = 0
    for i in range(n1):
        arr = []
        for j in range(n2):
            if grid[i][j] == 2:
                q.append(((i, j), 0))
                arr.append(True)
            elif grid[i][j] == 1:
                cnt += 1
                arr.append(False)
            else:
                arr.append(False)
        vis.append(arr)
    dRow = [-1, 0, 1, 0]
    dCol = [0, -1, 0, 1]
    cnt2 = 0
    while q:
        node = q.popleft()
        row = node[0][0]
        col = node[0][1]
        t = node[1]
        time = max(time, t)
        for i in range(4):
            nRow = row + dRow[i]
            nCol = col + dCol[i]
            if (
                nRow >= 0
                and nRow < n1
                and nCol >= 0
                and nCol < n2
                and not vis[nRow][nCol]
                and grid[nRow][nCol] == 1
            ):
                q.append((nRow, nCol), t + 1)
                vis[nRow][nCol] = True
                cnt2 += 1
    if cnt2 != cnt:
        return -1
    return time


print(orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
