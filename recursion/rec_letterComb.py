def letterCombinations(digs):
    n = len(digs)
    hash = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"  
    }
    res = []
    st = ""
    def dfs(i,st):
        print(st)
        if i == n:
            res.append(st)
            return
        curStr = hash[digs[i]]
        n2 = len(digs[i])
        for x in range(n2):
            st += curStr[x]
            dfs(i+1,st)
    dfs(0,"")
    return res
print(letterCombinations("23"))
    