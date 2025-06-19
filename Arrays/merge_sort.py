
def merge(arr,low,mid,high):
    
    left = low
    right = mid+1
    tmp = []
    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            tmp.append(arr[left])
            left += 1
        else:
            tmp.append(arr[right])
            right += 1


    while left <= mid:
        tmp.append(arr[left])
        left += 1

    while right <= high:
        tmp.append(arr[right])
        right += 1

    arr[low:high+1] = tmp



def mergeSort(arr,low,high):
    print(arr[low:high+1])
    if low >= high:
        return
    mid = (low+high)//2
    print(low,mid,high)
    mergeSort(arr,low,mid)
    mergeSort(arr,mid+1,high)
    
    merge(arr,low,mid,high)
    

arr = [2, 4, 1, 3, 5]
mergeSort(arr, 0, len(arr) - 1)
print(arr)