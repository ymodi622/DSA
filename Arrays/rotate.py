import numpy as np
def rotate(arr):
    tmp = arr[len(arr) - 1]
    for i in range(len(arr)-2,-1,-1):
        arr[i+1] = arr[i]
    arr[0] = tmp

k = int(input("Ener: "))
arr = np.array([1,2,3,4,5])
for i in range(k):
    rotate(arr)

print(arr)