def findFloor(arr,k):
    # res <= k
    low = 0
    high = len(arr)-1
    
    res = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] <= k:
            
            res = mid
            low = mid+1
        else:
            high = mid - 1
        
    return res

findFloor([1, 2, 8],1)