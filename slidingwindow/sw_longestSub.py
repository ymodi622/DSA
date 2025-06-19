def lengthOfLongestSubstring(s) -> int:
    n = len(s)
    l = 0
    r = 0
    hashArr = {}
    maxLen = 0  
    while r < n:
        if s[r] in hashArr:
            if hashArr[s[r]] >= l:
                
                l = hashArr[s[r]]+1
        lenSub = l-r+1
        maxLen = max(maxLen,lenSub) 
        hashArr[s[r]] = r
        r+=1
    return maxLen