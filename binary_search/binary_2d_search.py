def searchMatrix(mat,k) -> bool:
    m = len(mat)
    n = len(mat[0])
    for i in range(m):
        if k >= mat[i][0] and k <= mat[i][0]:
            low = 0
            high = n-1
            while low <= high:
                mid = (low+high)//2
                print(mat[i][mid])
                if mat[i][mid] > k:
                    high = mid-1
                elif mat[i][mid] < k:
                    low = mid+1
                else:
                    return True
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
            