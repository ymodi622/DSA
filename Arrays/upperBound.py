def findCeil(arr,k):
    arr.sort()
    low = 0
    high = len(arr)-1

    floor = -1
    
    while low <= high:
        mid = (low+high)//2
        if arr[mid] <= k:
            floor = arr[mid]
            low = mid+1
        else:
            high = mid - 1

    low = 0
    high = len(arr)-1
    ceil = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] >= k:
            ceil = arr[mid]
            high = mid - 1
        else:
            low = mid+1
    return floor,ceil

print(findCeil([36, 82, 88, 56, 21, 17, 73, 86],17))