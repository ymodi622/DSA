from collections import deque


class Solution:
    def updateMatrix(self, mat):
        n = len(mat)
        m = len(mat[0])
        res = []
        q = deque()
        vis = []
        for i in range(n):
            tmp = []
            tmp2 = []
            for j in range(m):
                if mat[i][j] == 0:
                    q.append(((i, j), 0))
                    tmp2.append(True)
                else:
                    tmp2.append(False)
                tmp.append(0)
            vis.append(tmp2)
            res.append(tmp)
        dRow = [-1, 0, 1, 0]
        dCol = [0, -1, 0, 1]
        while q:
            node = q.popleft()
            r = node[0][0]
            c = node[0][1]
            res[r][c] = node[1]
            for i in range(4):
                row = r + dRow[i]
                col = c + dCol[i]
                if row >= 0 and row < n and col >= 0 and col < m and not vis[row][col]:
                    q.append(((row, col), node[1] + 1))
                    vis[row][col] = True
        return res
