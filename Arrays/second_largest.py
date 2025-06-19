def getSecondLargest(arr):
    max1 = -1
    max2 = -1
    for i in range(len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2 and arr[i] != max1:
            max2 = arr[i]
    return max2   

print(getSecondLargest([10,10,10]))