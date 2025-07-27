def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


print(bubbleSort([5, 1, 9, 6, 3, 8, 7]))
