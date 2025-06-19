def addOperators(num, target):
    n = len(num)
    ops = n-1
    res = []
    subEq = ""
    ind = 0
    def dfs(ind,ans,subEq):
        print(ind,ans,subEq)
        if ind == n:
            print("in:",ans,subEq)
            if ans == target:
                res.append(subEq)
            return
        if ind == 0:
            tmp = subEq + num[ind]
        else:
            tmp = subEq + "+" + num[ind] 
        dfs(ind+1,ans+int(num[ind]),tmp)
        if ind == 0:
            tmp = subEq + num[ind]
        else:
            tmp = subEq + "-" + num[ind] 
        dfs(ind+1,ans-int(num[ind]),tmp)
        if ind == 0:
            tmp = subEq + num[ind]
        else:
            tmp = subEq + "*" + num[ind] 
        dfs(ind+1,ans*int(num[ind]),tmp)

    dfs(0,0,"")
        
    return res
print(addOperators("232",8))    