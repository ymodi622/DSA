def searchMatrix(mat,k) -> bool:
    m = len(mat)
    n = len(mat[0])
    row = 0
    col = n-1
    while row < m and col < n and row >= 0 and col >= 0:
        if mat[row][col] == k:
            return row+1,col+1
        elif mat[row][col] > k:
            col -= 1
        else:
            row += 1

        
    return -1,-1
print(searchMatrix([[-5]],-10))