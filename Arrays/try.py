import numpy as np
def traffic(x,n,arr):
    res = []
    res[len(res)-1] = x
    ind = 1
    print(res)
    for i in range(len(arr)):
        while arr[i] > res[ind]:
            print(arr[i])
            print(ind)
            ind += 1

        res[ind] = arr[i]
        ind = 1
    print(res)

traffic(8,3,[3,6,2])
