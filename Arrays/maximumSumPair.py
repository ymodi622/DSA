from collections import defaultdict
def maximumSum(arr):
    def digSum(n):
        st = str(n)
        sm = 0
        for i in st:
            sm += int(i)

        return sm
    res = -1
    hashArr = defaultdict(list)
    for i in range(len(arr)):
        d = digSum(arr[i])
        hashArr[d].append(i)
        
    for i in hashArr:
        if len(hashArr[i])>1:
            tmp = hashArr[i]
            mx1 = tmp[0]
            for i in tmp:
                mx1 = max(mx1,arr[i])
            tmp.remove(arr.index(mx1))
            mx2 = tmp[0]
            for i in tmp:
                mx2 = max(mx2,arr[i])
            res = max(res,mx1+mx2)

    return res    

print(maximumSum([229,398,269,317,420,464,491,218,439,153,482,169,411,93,147,50,347,210,251,366,401]))