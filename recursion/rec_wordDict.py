# def wordBreak(s, wordDict) -> bool:
#     n = len(s)
#     ind = 0
#     sub = ""
#     ptr = 0
#     while ind < n:
#         sub += s[ind]
#         if sub in wordDict:
#             ptr = ind+1
#             sub = ""
#         print(sub,ptr)
#         ind += 1
#     if ptr != n:
#         return False
#     return True
# wordBreak("aaaaaaa",["aaaa","aaa"])

def wordBreak(s, wordDict) -> bool:
    n = len(s)
    res = False
    def dfs(ind):
        sub = ""
        if ind == n:
            return
        for i in range(ind,n):
            sub += s[ind]
            if sub in wordDict:
                dfs()
        