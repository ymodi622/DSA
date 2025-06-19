def searchRange(arr, k):
    # if k not in arr:
    #     return -1,-1
    # low = 0
    # high = len(arr)-1

    # lb = -1

    # while low <= high:
    #     mid = (low+high)//2
    #     if arr[mid] >= k:
    #         lb = mid
    #         high = mid-1
    #     else:
    #         low = mid+1

    # low = 0
    # high = len(arr)-1

    # ub = -1

    # while low <= high:
    #     mid = (low+high)//2
    #     if arr[mid] <= k:
    #         ub = mid
    #         low = mid+1   
    #     else:
    #         high = mid-1
    # return lb,ub 
    low = 0
    high = len(arr)-1
    st = 10**4
    end = 0
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == k:
            high = mid-1
            st = min(st,mid)
        elif arr[mid] < k:
            low = mid+1
        else:
            high = mid-1
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == k:
            low = mid+1
            end = max(end,mid)
        elif arr[mid] < k:
            low = mid+1
        else:
            high = mid-1
    return end-st+1

print(searchRange([8, 9, 10, 12, 12, 12],12))