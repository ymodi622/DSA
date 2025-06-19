def search(arr,k):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == k:
            return True
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            
            low = low + 1
            high = high - 1
            continue
        if arr[low] <= arr[mid]:
            if arr[low] <= k and k <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] <= k and k <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return False

print(search([1,0,1,1,1],0))