from collections import deque


def floodFill(image, sr, sc):
    m = len(image[0])
    n = len(image)
    vis = [[False for j in range(m)] for i in range(n)]
    vis[sr][sc] = True
    q = deque()
    q.append((sr, sc))
    image[sr][sc] = 2
    dRow = [-1, 0, 1, 0]
    dCol = [0, -1, 0, 1]
    while q:
        node = q.popleft()
        r = node[0]
        c = node[1]
        for i in range(4):
            row = r + dRow[i]
            col = c + dCol[i]
            if (
                row >= 0
                and row < n
                and col >= 0
                and col < m
                and image[row][col] == 1
                and not vis[row][col]
            ):
                image[row][col] = 2
                vis[row][col] = True
                q.append((row, col))

    return image


print(floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1))
