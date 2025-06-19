def solve( arr, k):
    cnt = 0
    hashArr = {0:1}
    xr = 0
    cnt = 0
    for i in range(len(arr)):
        xr = arr[i] ^ xr
        tmp = xr ^ k
        if tmp in hashArr.keys():
            cnt += hashArr[tmp]
        if xr not in hashArr.keys():
            hashArr[xr] = 1
        else:
            hashArr[xr] += 1
        
        
    return cnt
        

print(solve([ 1, 2, 2, 3 ],0))