def findMinArea(grid):
    if not grid:
        return float("inf")
    n, m = len(grid), len(grid[0])
    minRow, maxRow, minCol, maxCol = float("inf"), -1, float("inf"), -1

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                minRow = min(minRow, i)
                minCol = min(minCol, j)
                maxRow = max(maxRow, i)
                maxCol = max(maxCol, j)
    return (maxRow - minRow + 1) * (maxCol - minCol + 1)


def rotate(grid, n, m):
    arr = []
    for j in range(m):
        tmp = []
        for i in range(n - 1, -1, -1):
            tmp.append(grid[i][j])
        arr.append(tmp)

    return arr


def main(grid):

    res = float("inf")

    for _ in range(4):
        n = len(grid)
        m = len(grid[0])
        for i in range(1, n):
            a1 = findMinArea(grid[i:])
            for j in range(m):
                split2 = [row[:j] for row in grid[:i]]
                split3 = [row[j:] for row in grid[:i]]
                a2 = findMinArea(split2)
                a3 = findMinArea(split3)
                res = min(res, a1 + a2 + a3)
            for i2 in range(0, i):
                split2 = grid[0:i2]
                split3 = grid[i2:i]
                a2 = findMinArea(split2)
                a3 = findMinArea(split3)
                res = min(res, a1 + a2 + a3)
        grid = rotate(grid, n, m)
    return res


print(main([[1, 0, 1, 0], [0, 1, 0, 1]]))
