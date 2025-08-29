import time
import random
import matplotlib.pyplot as plt


def selectionSort(arr):
    for i in range(len(arr)):
        minInd = i
        for j in range(i + 1, len(arr)):
            if arr[minInd] > arr[j]:
                minInd = j
        arr[minInd], arr[i] = arr[i], arr[minInd]
    return arr


def measure_time(func, arr):
    start = time.time()
    func(arr.copy())
    end = time.time()
    return (end - start) * 1000


sizes = list(range(0, 1001, 20))
times = []

for size in sizes:
    arr = [random.randint(1, 10000) for _ in range(size)]
    t = measure_time(selectionSort, arr)
    times.append(t)


plt.figure(figsize=(10, 6))
plt.plot(sizes, times, marker="o", label="Iterative Selection Sort")
plt.xlabel("Input Size (n)")
plt.ylabel("Time (ms)")
plt.title("Time Complexity of Iterative Selection Sort (More Testcases)")
plt.legend()
plt.grid(True)
plt.show()
