def selectionSort(arr):
    for i in range(len(arr)):
        minInd = i
        for j in range(i + 1, len(arr)):
            if arr[minInd] > arr[j]:
                minInd = j
        arr[minInd], arr[i] = arr[i], arr[minInd]
    return arr


print(selectionSort([5, 1, 9, 6, 3, 8, 7]))
