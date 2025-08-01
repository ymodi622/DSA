def bubbleSort(arr):
    def compare(i):
        if i == len(arr) - 1:
            return

        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        compare(i + 1)

    compare(0)
    return arr


print(bubbleSort([5, 1, 9, 6, 3, 2]))
