import time
import random
import matplotlib.pyplot as plt


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


def measure_time(func, arr):
    start = time.time()
    func(arr.copy())
    end = time.time()
    return (end - start) * 1000


sizes = list(range(500, 5500, 500))
times = []

for size in sizes:
    arr = [random.randint(1, 10000) for _ in range(size)]
    t = measure_time(insertionSort, arr)
    times.append(t)


plt.figure(figsize=(10, 6))
plt.plot(sizes, times, marker="o", label="Iterative Insertion Sort")
plt.xlabel("Input Size (n)")
plt.ylabel("Time (ms)")
plt.title("Time Complexity of Iterative Insertion Sort (More Testcases)")
plt.legend()
plt.grid(True)
plt.show()
