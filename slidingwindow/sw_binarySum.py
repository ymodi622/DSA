def numSubarraysWithSum(arr, k) -> int:
    n = len(arr)
    l = 0
    r = 0
    cnt = 0
    sumTill = 0
    while r < n and l < n:
        if sumTill <= k:
            sumTill += arr[r]
            if sumTill == k:
                cnt += 1
            if sumTill <= k:
                r += 1
        else:
            sumTill -= arr[l]
            if sumTill == k:
                cnt += 1
            l += 1
            
        print(l,r)
        print("sum",sumTill)
        print("cnt",cnt)
            
numSubarraysWithSum([1,0,0,1,1,0,],2)