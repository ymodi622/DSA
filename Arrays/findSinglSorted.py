def singleNonDuplicate(arr) -> int:
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[low] != arr[low+1]:
            return arr[low]
        elif arr[high] != arr[high-1]:
            return arr[high]


        if arr[mid] == arr[mid-1]:
            if ((mid-2)-low)%2 == 0:
                high = mid-2
            else:
                low = mid+1
                
        elif arr[mid] == arr[mid+1]:
            if ((mid+2)-high)%2 == 0:
                low = mid+2
            else:
                high = mid-1
        else:
            return arr[mid]
        # print(low,mid,high)
print(singleNonDuplicate([1,1,2,3,3,4,4,8,8]))