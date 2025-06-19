def sumOfAllSUbs(arr):
    res = []
    n = len(arr)
    sub = []
    def dfs(i,s):
        if i == n:
            res.append(s)
            return
        s+=arr[i]
        dfs(i+1,s)
        s -= arr[i]
        dfs(i+1,s)
    dfs(0,0)
    return res
print("res:",sumOfAllSUbs([3,1,2])) 