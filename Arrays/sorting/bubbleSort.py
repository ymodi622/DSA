def bubbleSort(arr):
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]

    return arr


print(bubbleSort([5, 1, 9, 6, 3, 8, 7]))
