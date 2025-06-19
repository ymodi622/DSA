def merge(arr,low,mid,high,cnt):
    left = low
    right = mid+1
    tmpRight = mid+1
    tmp = []
    stick = 0
    for i in range(low,mid+1):
        while tmpRight <= high and arr[i] > arr[tmpRight]*2:
            stick += 1
            tmpRight += 1
        cnt[0] += stick 
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





def mergeSort(arr,low,high,cnt):
    if low >= high:
        return
    mid = (low+high)//2
    mergeSort(arr,low,mid,cnt)
    mergeSort(arr,mid+1,high,cnt)
    merge(arr,low,mid,high,cnt)
    

arr = [40,25,19,12,9,6,2]
cnt = [0] 
mergeSort(arr, 0, len(arr) - 1, cnt)
print(cnt[0])