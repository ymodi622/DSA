def sortMatrix(grid):
    n = len(grid)
    res = [[-1 for _ in range(n)] for _ in range(n)]
    print(res)
    row = 0
    col = 0

    def sortReplace(row, col, flag):

        r, c = row, col
        arr = []
        while row < n and col < n:
            arr.append(grid[row][col])
            row += 1
            col += 1
        if flag:
            arr.sort(reverse=True)
        else:
            arr.sort()
        row, col = r, c
        for i in range(len(arr)):
            res[row][col] = arr[i]
            row += 1
            col += 1

    for i in range(n - 1, 0, -1):
        sortReplace(0, i, False)
    for i in range(n):
        sortReplace(i, 0, True)
    return res


print(sortMatrix([[1, 7, 3], [9, 8, 2], [4, 5, 6]]))
