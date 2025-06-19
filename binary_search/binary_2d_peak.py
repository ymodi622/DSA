def findPeakGrid(mat):
    m = len(mat)
    
    n = len(mat[0])
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        maxi = 0
        col = mid
        for i in range(m):
            if mat[i][mid] > maxi:
                maxi = mat[i][mid]
                row = i
        if row != 0 and col != 0 and row!= m-1 and col != n-1:
            if mat[row][col] > mat[row][col+1] and mat[row][col] > mat[row][col-1]:
                return row,col
            else:
                if mat[row][col] < mat[row][col+1]:
                    low = mid+1
                if mat[row][col] < mat[row][col-1]:
                    high = mid-1
        elif col == n-1:
            if mat[row][col] > mat[row][col-1]:
                return row,col
            else:
                high = mid-1
        elif col == 0:
            if mat[row][col] > mat[row][col+1]:
                return row,col
            else:
                low = mid+1
        elif row == m-1:
            if mat[row][col] > mat[row-1][col] and mat[row][col] > mat[row][col+1] and mat[row][col] > mat[row][col-1]:
                return row,col
            else:
                if mat[row][col] < mat[row][col+1]:
                    low = mid+1
                if mat[row][col] < mat[row][col-1]:
                    high = mid-1
        elif row == 0:
            if mat[row][col] > mat[row+1][col] and mat[row][col] > mat[row][col+1] and mat[row][col] > mat[row][col-1]:
                return row,col
            else:
                if mat[row][col] < mat[row][col+1]:
                    low = mid+1
                if mat[row][col] < mat[row][col-1]:
                    high = mid-1
print(findPeakGrid([[25,37,23,37,19],[45,19,2,43,26],[18,1,37,44,50]]))