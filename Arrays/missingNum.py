from collections import defaultdict
def findTwoElement(arr):
    hashArr = defaultdict(int)
    elem = 1
    for i in range(1,len(arr)+1):
        hashArr[elem] = 0
        elem += 1
    for i in range(len(arr)):
        hashArr[arr[i]] += 1
    miss = -1
    mn = -1

    for i in hashArr:
        if hashArr[i] == 2:
            mn = i
        elif hashArr[i] == 0:
            miss = i
        if miss != -1 and mn != -1:
            break

    return [mn,miss]

print(findTwoElement([5, 1, 6, 2, 4, 6]))
