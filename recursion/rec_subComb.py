def combinationSum3(k,n):
    if k > n:
        return []
    res = []
    sub = []
    def dfs(num,cnt,s):
        print(sub)
        print(num,cnt,s)
        if s > n:
            return
        if cnt == k:
            print("hii",s)
            if s == n:
                res.append(sub.copy())
            return
        if cnt == k-1:
            rem = n-s
            if rem > 9:
                return
        for i in range(num+1,n):
            s += i
            sub.append(i)
            dfs(i,cnt+1,s)
            s -= i
            sub.pop()
    dfs(0,0,0)
    return res
print(combinationSum3(2,18))