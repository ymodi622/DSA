def characterReplacement(s: str, k: int) -> int:
    n = len(s)
    l = 0
    r = 0
    cnt = 0
    hash = {}
    maxLen = 0
    maxFeq = 0
    while r < n:
        if s[r] not in hash.keys():
            hash[s[r]] = 1
        else:
            hash[s[r]] += 1
        maxFeq = max(maxFeq,hash[s[r]])
        maxi = r - l + 1
        if maxi - maxFeq > k:
            hash[s[l]] -= 1
            l += 1
            maxFeq = max(maxFeq,hash[s[l]])
        maxi = r - l + 1
        maxLen = max(maxLen,maxi)
        print("l:",l,"r:",r)
        print("hash:",hash)
        print(maxLen)
        r += 1
    return maxLen
        
characterReplacement("abab",0)
                 