def findMin(arr) -> int:
    low = 0
    high = len(arr)-1
    res = 10**4
    while low <= high:
        mid = (low+high)//2
        res = min(res,arr[low],arr[mid],arr[high])
        low += 1
        high -= 1

    return res
print(findMin([3,4,5,1,2]))