import numpy as np
def rotate(arr,k):
    tmp = np.zeros(k)
    ind =  0
    for i in range(k,0,-1):
        tmp[ind] = arr[len(arr) - i]
        ind += 1
    for i in range(len(arr)-k-1,-1,-1):
        arr[i+k] = arr[i]
    for i in range(k):
        arr[i] = tmp[i]

arr = np.array([-1])
k = int(input("Enter: "))
if k > len(arr):
    rotate(arr, k%len(arr))
elif k < len(arr):
    rotate(arr,k)
print(arr)
