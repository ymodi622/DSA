def selectionSort(arr):
    for i in range(len(arr)):
        minInd = i
        for j in range(len(arr) - 1, i - 1, -1):
            if arr[minInd] > arr[j]:
                minInd = j
        arr[minInd], arr[j] = arr[j], arr[minInd]
    return arr


print(selectionSort([5, 1, 9, 6, 3, 8, 7]))
