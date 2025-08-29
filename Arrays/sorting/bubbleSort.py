import time
import random
import matplotlib.pyplot as plt


def bubbleSort(arr):
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
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
plt.plot(sizes, times, marker="o", label="Iterative Bubble Sort")
plt.xlabel("Input Size (n)")
plt.ylabel("Time (ms)")
plt.title("Time Complexity of Iterative Bubble Sort (More Testcases)")
plt.legend()
plt.grid(True)
plt.show()
