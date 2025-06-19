import numpy as np
def reverse(arr,n):
    for i in range(n//2):
        arr[i],arr[n-i-1] = arr[n-i-1],arr[i]

    return arr

arr = np.array([1,2,3,4,5])
k = int(input("Enter: "))
n = len(arr)
arr1 = reverse(arr[:k],k)
arr2 = reverse(arr[k:],n-k)
arr = np.concatenate(arr1,arr2)
print(arr)