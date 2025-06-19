def subsetsWithDup(arr):
    arr.sort()
    res = [[]]
    n = len(arr)
    sub = []
    def dfs(i):
        print("sub:",sub)
        print("i:",i)
        if i == n:
            return
        tmp = i
        while tmp < n:
            print(tmp)
            if tmp > i and arr[tmp] == arr[tmp-1]:
                tmp += 1
                continue
            sub.append(arr[tmp])
            res.append(sub.copy())
            dfs(tmp+1)
            sub.pop()
            tmp += 1
            
    dfs(0)
    return res
print(subsetsWithDup([1,2,2,3,3]))