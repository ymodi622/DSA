mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n = len(mat)
m = len(mat[0])
size = n*m
n = 0
m = 0
print("size",size)
limit = n
def spin(mat,n,m,limit,cnt):
    
    while m < limit-1:
        m += 1
        print(mat[n][m])
        cnt += 1
    
    while n < limit-1:
        n += 1
        print(mat[n][m])
        cnt += 1

    while m > len(mat)-limit:
        m -= 1
        print(mat[n][m])
        cnt += 1

    while n > (len(mat)-limit)+1:
        n -= 1
        print(mat[n][m])
        cnt += 1

    
    return n,m,cnt
    
print(mat[0][0])
cnt = 1
limit = len(mat)
while cnt < size:
    n,m,cnt = spin(mat,n,m,limit,cnt)
    if cnt >= size:
        break
    print("cnt",cnt)
    limit -= 1
    n,m,cnt = spin(mat,n,m,limit,cnt)
    if cnt >= size:
        break
    print("cnt",cnt)
