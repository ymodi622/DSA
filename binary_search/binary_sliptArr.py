def splitArray(arr, k):
    def finSeg(arr,tar):
        segCnt = 1
        cnt = 0
        for i in range(len(arr)):
            if cnt + arr[i] <= tar:
                cnt += arr[i]
            else:
                segCnt += 1
                cnt = arr[i]
        return segCnt
    low = max(arr)
    high = sum(arr)
    for i in range(low,high+1):
        mid = (low+high)//2
        segCnt =  finSeg(arr,mid)
        if segCnt <= k:
            high = mid -1
        else:
            low = mid+1
    return low
       
print(splitArray([7,2,5,10,8],2))