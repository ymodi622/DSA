arr = [2,3,4,7,11]
k = 5
val = 1
ind = 0
res = val
while val <= k:
    while arr[ind] == val:
        ind += 1
        val += 1
    print(res,val)
    res = arr[ind]
    val += 1

print(res)