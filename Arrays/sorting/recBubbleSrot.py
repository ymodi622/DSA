import sys
import time
import random
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)


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


def measure_time(func, arr):
    start = time.time()
    func(arr.copy())
    end = time.time()
    return (end - start) * 1000


sizes = list(range(0, 1001, 20))
times = []

for size in sizes:
    arr = [random.randint(1, 10000) for _ in range(size)]
    t = measure_time(bubbleSort, arr)
    times.append(t)


plt.figure(figsize=(10, 6))
plt.plot(sizes, times, marker="o", label="Recursive Bubble Sort")
plt.xlabel("Input Size (n)")
plt.ylabel("Time (ms)")
plt.title("Time Complexity of Recursive Bubble Sort (More Testcases)")
plt.legend()
plt.grid(True)
plt.show()
