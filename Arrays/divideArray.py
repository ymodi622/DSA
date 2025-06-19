def divideArray(arr, k):
    arr.sort()
    if len(arr) % 3 != 0:
        return []
    res = []
    tmp = []
    for i in range(len(arr)):
        print(tmp, res)
        tmp.append(arr[i])
        if i + 1 >= 3 and (i + 1) % 3 == 0:
            if tmp[-1] - tmp[0] > k:
                return []
            res.append(tmp)
            tmp = []
    return res


print(divideArray([2, 4, 2, 2, 5, 2], 2))
