def fruitsIntoBaskets(arr,k) -> int:
    n = len(arr)
    l = 0
    r = 0
    hashArr = {}
    maxLen = 0
    while r < n:
        if arr[r] not in hashArr:
            if len(hashArr) < k:
                hashArr[arr[r]] = 1
            else:
                print("hii")
                hashArr[arr[l]] -= 1
                if hashArr[arr[l]] == 0:
                    hashArr.pop(arr[l])
                l += 1
                continue
        else:
            hashArr[arr[r]] += 1
        if len(hashArr) <= k:
            frtLen = r - l + 1
            maxLen = max(maxLen,frtLen)
        print("l:",l,"r:",r)
        print("length:",len(hashArr))
        print(hashArr)
        print("max",maxLen)
        r += 1
print(fruitsIntoBaskets([3,3,3,1,2,1,1,2,3,3,4],2))