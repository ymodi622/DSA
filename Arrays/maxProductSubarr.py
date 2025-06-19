def maxProduct(arr):
    res = -10**4
    pre = 1
    suf = 1
    n = len(arr)-1
    for i in range(n+1):
        if pre == 0:pre = 1
        if suf == 0:suf = 1
        pre *= arr[i]
        suf *= arr[n-i]
        res = max(res,max(pre,suf))

        
    return res

print(maxProduct([-3,0,1,-2]))
