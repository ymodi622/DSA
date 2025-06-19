def longestOnes(arr,k) -> int:
    n = len(arr)
    l = 0
    r = 0
    zeroes = 0
    maxLen = 0
    
    while r < n:
        if zeroes > k:
            if arr[l] == 0:
                zeroes -= 1
            l += 1
        if arr[r] == 0:
            zeroes += 1
        oneLen = r - l + 1
        if zeroes <= k:
            maxLen = max(maxLen,oneLen)    
        r += 1
            
       
longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3)  