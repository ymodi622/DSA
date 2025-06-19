def findpageCnt(arr, n, m):
    if m > n:
        return -1
    def numStuds(arr,pages):
        stCnt = 1
        pageCnt = 0
        for i in range(n):
            if arr[i]+pageCnt <= pages:
                pageCnt += arr[i]
            else:
                stCnt += 1
                pageCnt = arr[i]
        return stCnt
    low = max(arr)
    high = sum(arr)
    while low <= high:
        mid = (low+high)//2
        stCnt = numStuds(arr,mid)
        if stCnt <= m:
            high = mid-1
        else:
            low = mid+1
    return low
print(findpageCnt([12, 34, 67, 90],4,2))