def pointerSort(arr):
    low = 0
    mid = 0
    high = len(arr)-1
    while mid <= high:
        if arr[mid] == 0:
            arr[mid],arr[low] = arr[low],arr[mid]
            mid += 1
            low += 1

        elif arr[mid] == 2:
            arr[high],arr[mid] = arr[mid],arr[high]
            # mid += 1
            high -= 1

        else:
            mid += 1

    return arr

print(pointerSort([1,2,2,0,1,0,2]))