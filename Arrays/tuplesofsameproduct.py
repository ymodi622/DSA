def tupleSameProduct(arr):
    resArr = []
    res  = 0
    hashArr = {}
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            ans = arr[i]*arr[j]
            if ans not in hashArr.keys():
                hashArr[ans] = 1
            else:
                hashArr[ans] += 1

    for i in hashArr.values():
        if i > 1:
            res += i*(i-1) // 2
        
    return res*8

print(tupleSameProduct([2,3,4,6,8,12]))