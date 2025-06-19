def maxKdistinctSubarray(s,k)->int:
    n = len(s)
    l = 0
    r = 0
    maxLen = 0
    hash = {}
    while r < n:
        if s[r] not in hash:
            hash[s[r]] = 1
        else:
            hash[s[r]] += 1
        if len(hash) > k:
            hash[s[l]] -= 1
            if hash[s[l]] == 0:
                hash.pop(s[l])
            l += 1
        if len(hash) <= k:
            maxLen = max(maxLen,r-l+1)
        print("max:",maxLen)
        print(hash)
        print(l,r)
        r += 1
maxKdistinctSubarray("aaabbccd",2)