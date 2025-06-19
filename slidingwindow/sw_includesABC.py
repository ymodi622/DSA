def numberOfSubstrings(s: str) -> int:
    cnt = 0
    hash = {"a":-1,"b":-1,"c":-1}
    for i in range(len(s)):
        hash[s[i]] = i
        if hash["a"] != -1 and hash["b"] != -1 and hash["c"] != -1:
            cnt += min(hash["a"],hash["b"],hash["c"])+1
    return cnt
print(numberOfSubstrings("aaabc"))