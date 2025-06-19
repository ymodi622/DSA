def partition(s: str):
    n = len(s)
    res = []
    path = []
    def dfs(i,path):
        print(i,path)
        if i == n:
            res.append(path.copy())
            return
        for x in range(i,n):
            sub = s[i:x+1]
            print("sub:",sub,i,x)
            if sub == sub[::-1]:
                path.append(sub)
                dfs(x+1,path)
                path.pop()           
                
            
    dfs(0,[])
    return res
print(partition("aab"))