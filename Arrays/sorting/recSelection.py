def selectionSort(arr):
    def compare(i):
        if i == len(arr) - 1:
            return
        minInd = i
        for j in range(len(arr) - 1, i - 1, -1):
            if arr[minInd] > arr[j]:
                minInd = j
        arr[minInd], arr[j] = arr[j], arr[minInd]
        compare(i + 1)

    compare(0)
    return arr


print(selectionSort([5, 1, 9, 6, 3, 8, 7]))
