def findKRotation(arr):
    low = 0
    high = len(arr)-1
    res = -1
    mid = (low+high)//2
    if arr[low] < arr[mid] and arr[mid] < arr[high]:
        return 0

    while low <= high:
        mid = (low+high)//2
        if arr[low] <= arr[mid] and arr[mid] <= arr[high]:
            res = max(res,arr[high])
            break
        if arr[low] >= arr[mid] and arr[low]>=arr[high]:
            res = max(res,arr[low])
            high = mid-1
        elif arr[low] <= arr[mid] and arr[mid] >= arr[high]:
            res = max(res,arr[mid])
            low = mid + 1


    res = arr.index(res)+1
    return res

print(findKRotation([3,4,5,1,2]))